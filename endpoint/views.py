from django.shortcuts import render
from .models import StringModel
from .serializers import StringSerializers
from rest_framework import viewsets


# Create your views here.
class StringViewSet(viewsets.ModelViewSet):
    queryset = StringModel.objects.all()
    serializer_class = StringSerializers
