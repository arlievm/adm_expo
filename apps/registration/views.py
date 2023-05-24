from django.shortcuts import render
from rest_framework import generics

from .serializers import ApplicationSerializer
from .models import Application


class ApplicationCreateListView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    
    
class ApplicationDeleteView(generics.DestroyAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()