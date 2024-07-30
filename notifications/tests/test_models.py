# notifications/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from ..infrastructure.models import Notification

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.notification = Notification.objects.create(
            recipient=self.user,
            message="Test notification"
        )

    def test_notification_creation(self):
        self.assertEqual(self.notification.recipient.username, 'testuser')
        self.assertEqual(self.notification.message, "Test notification")
        self.assertFalse(self.notification.is_read)

    def test_notification_str_method(self):
        self.assertEqual(str(self.notification), f"Notification to testuser - Test notification")
