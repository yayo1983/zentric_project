# notifications/tests/test_integration.py
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Notification
from ..utils import send_notification

class NotificationIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_send_notification_creates_entry(self):
        send_notification(self.user, "Integration test notification")
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.message, "Integration test notification")
        self.assertEqual(notification.recipient, self.user)
