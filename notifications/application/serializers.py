from rest_framework import serializers
from ..infrastructure.models import Notification
from shareds.application.abstract_serializer import AbstractSerializer, CommonMetaClass

class NotificationSerializer(AbstractSerializer, serializers.ModelSerializer, metaclass=CommonMetaClass):
    
    def get_serializer_class(self):
        return NotificationSerializer
    
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'message', 'created_at', 'is_read']
    

