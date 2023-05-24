from django.shortcuts import render
from rest_framework import generics

from .serializers import ApplicationENSerializer
from .models import ApplicationEN


class ApplicationCreateListView(generics.ListCreateAPIView):
    serializer_class = ApplicationENSerializer
    queryset = ApplicationEN.objects.all()
    
    
class ApplicationDeleteView(generics.DestroyAPIView):
    serializer_class = ApplicationENSerializer
    queryset = ApplicationEN.objects.all()