from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.response import Response
from .models import StringModel
from .serializers import StringSerializers
from .filters import StringFilter
from rest_framework import status
from rest_framework import serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StringViewSet(viewsets.ModelViewSet):
    queryset = StringModel.objects.all()
    serializer_class = StringSerializers
    lookup_field ='value'
    filter_backends = [DjangoFilterBackend]
    filterset_class = StringFilter

    def create(self, request):
        try:
            serializer = get_serializer(data=request.data)
            serializer.is_valid(raise_exception = True)
        except ValidationError as e:
            return Response(e.detail, status=422)
