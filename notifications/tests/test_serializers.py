from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from ..application.serializers import NotificationSerializer

class NotificationSerializerTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username="sender", password="12345", is_active=True)
        self.recipient = User.objects.create_user(username="recipient", password="12345", is_active=True)
        self.inactive_recipient = User.objects.create_user(username="inactive_recipient", password="12345", is_active=False)

        self.factory = APIRequestFactory()

        self.valid_data = {
            "recipient": self.recipient.id,
            "message": "Este es un mensaje de prueba válido.",
            "created_at": "2024-08-02T12:00:00Z",
            "is_read": False
        }
        self.invalid_data_message_empty = {
            "recipient": self.recipient.id,
            "message": "  ",
            "created_at": "2024-08-02T12:00:00Z",
            "is_read": False
        }
        self.invalid_data_message_short = {
            "recipient": self.recipient.id,
            "message": "Hola",
            "created_at": "2024-08-02T12:00:00Z",
            "is_read": False
        }
        self.invalid_data_inactive_recipient = {
            "recipient": self.inactive_recipient.id,
            "message": "Este es un mensaje de prueba válido.",
            "created_at": "2024-08-02T12:00:00Z",
            "is_read": False
        }
        self.invalid_data_self_recipient = {
            "recipient": self.sender.id,
            "message": "Este es un mensaje de prueba válido.",
            "created_at": "2024-08-02T12:00:00Z",
            "is_read": False
        }

    def test_notification_serializer_with_valid_data(self):
        request = self.factory.post('/')
        request.user = self.sender
        serializer = NotificationSerializer(data=self.valid_data, context={'request': request})
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_notification_serializer_with_empty_message(self):
        request = self.factory.post('/')
        request.user = self.sender
        serializer = NotificationSerializer(data=self.invalid_data_message_empty, context={'request': request})
        self.assertFalse(serializer.is_valid())
        self.assertIn('message', serializer.errors)

    def test_notification_serializer_with_short_message(self):
        request = self.factory.post('/')
        request.user = self.sender
        serializer = NotificationSerializer(data=self.invalid_data_message_short, context={'request': request})
        self.assertFalse(serializer.is_valid())
        self.assertIn('message', serializer.errors)

    def test_notification_serializer_with_inactive_recipient(self):
        request = self.factory.post('/')
        request.user = self.sender
        serializer = NotificationSerializer(data=self.invalid_data_inactive_recipient, context={'request': request})
        self.assertFalse(serializer.is_valid())
        self.assertIn('recipient', serializer.errors)

    def test_notification_serializer_with_self_recipient(self):
        request = self.factory.post('/')
        request.user = self.sender
        serializer = NotificationSerializer(data=self.invalid_data_self_recipient, context={'request': request})
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)
