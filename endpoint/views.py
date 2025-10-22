from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
import hashlib
from .models import StringModel
from .serializers import StringSerializers

class StringViewSet(viewsets.ModelViewSet):
    queryset = StringModel.objects.all().order_by('-created_at')
    serializer_class = StringSerializers

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            # Return 422 instead of DRF default 400
            return Response(e.detail, status=422)

        value = serializer.validated_data['value']
        length = len(value)
        sha256 = hashlib.sha256(value.encode('utf-8')).hexdigest()
        is_palindrome = value.lower() == value.lower()[::-1]

        try:
            obj = StringModel.objects.create(
                value=value,
                length=length,
                sha256=sha256,
                is_palindrome=is_palindrome
            )
        except IntegrityError:
            return Response(
                {"detail": "String already exists."},
                status=status.HTTP_409_CONFLICT
            )

        data = self.get_serializer(obj).data
        headers = {'Location': f"/strings/{obj.value}"}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

