from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group, Permission
from ..infrastructure.models import Notification


class NotificationAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="12345")

        self.create_permissions()

        product_group = Group.objects.create(name="test group")
        add_inventory_permission = Permission.objects.get(codename="add_notification")
        view_inventory_permission = Permission.objects.get(codename="view_notification")
        edit_inventory_permission = Permission.objects.get(codename="edit_notification")
        delete_inventory_permission = Permission.objects.get(
            codename="delete_notification"
        )
        product_group.permissions.add(
            add_inventory_permission,
            view_inventory_permission,
            edit_inventory_permission,
            delete_inventory_permission,
        )
        
        self.client.force_authenticate(user=self.user)

        self.notification = Notification.objects.create(
            recipient=self.user, message="Test notification"
        )
        self.url = reverse("notification-list")

    def create_permissions(self):
        if not Permission.objects.filter(codename="add_notification").exists():
            Permission.objects.create(
                codename="add_notification",
                name="Can add notification",
                content_type_id=Notification._meta.app_label,
            )
        if not Permission.objects.filter(codename="view_notification").exists():
            Permission.objects.create(
                codename="view_notification",
                name="Can view notification",
                content_type_id=Notification._meta.app_label,
            )

    # def test_list_notifications(self):
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)

    # def test_create_notification(self):
    #     data = {"recipient": self.user.id, "message": "Another notification"}
    #     response = self.client.post(self.url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_mark_as_read(self):
    #     url = reverse("notification-detail", kwargs={"pk": self.notification.id})
    #     response = self.client.patch(url, {"is_read": True})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.notification.refresh_from_db()
    #     self.assertTrue(self.notification.is_read)
