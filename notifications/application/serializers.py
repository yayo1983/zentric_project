from rest_framework import serializers
from ..infrastructure.models import Notification
from shareds.application.abstract_serializer import AbstractSerializer, CommonMetaClass
from django.contrib.auth.models import User

class NotificationSerializer(AbstractSerializer, serializers.ModelSerializer, metaclass=CommonMetaClass):
    recipient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    def get_serializer_class(self):
        return NotificationSerializer
    
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'message', 'created_at', 'is_read']
        read_only_fields = ['created_at'] 
        
    def validate_message(self, value):
        """
        Validation to ensure that the message is not empty
        and has a minimum length.
        """
        if not value.strip():
            raise serializers.ValidationError("El mensaje no puede estar vacío.")
        if len(value) < 10:
            raise serializers.ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return value

    def validate_recipient(self, value):
        """
        Custom validation to ensure the recipient is an active user.
        """
        if not value.is_active:
            raise serializers.ValidationError("El usuario destinatario debe estar activo.")
        return value

    def validate(self, data):
        """
        General validation to ensure that a user cannot
        send a notification to themselves.
        """
        if 'recipient' in data and self.context['request'].user == data['recipient']:
            raise serializers.ValidationError("No puedes enviarte una notificación a ti mismo.")
        return data
    

