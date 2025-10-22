from django.shortcuts import render
from .models import StringModel
from .serializers import StringSerializers
from .filters import StringFilter
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StringViewSet(viewsets.ModelViewSet):
    queryset = StringModel.objects.all()
    serializer_class = StringSerializers
    lookup_field ='value'
    filter_backends = [DjangoFilterBackend]
    filterset_class = StringFilter
