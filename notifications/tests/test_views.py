# notifications/tests/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..infrastructure.models import Notification

class NotificationAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.notification = Notification.objects.create(
            recipient=self.user,
            message="Test notification"
        )
        self.url = reverse('notification-list')

    def test_list_notifications(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_notification(self):
        data = {
            "recipient": self.user.id,
            "message": "Another notification"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_mark_as_read(self):
        url = reverse('notification-detail', kwargs={'pk': self.notification.id})
        response = self.client.patch(url, {"is_read": True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.notification.refresh_from_db()
        self.assertTrue(self.notification.is_read)
