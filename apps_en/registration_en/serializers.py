from .models import ApplicationEN
from rest_framework import serializers as s


class ApplicationENSerializer(s.Serializer):
    
    class Meta:
        model = ApplicationEN
        fields = 'name_organic', 'surname', 'name', 'email', 'number', 'user_status', 'id'