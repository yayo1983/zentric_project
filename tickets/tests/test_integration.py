from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..infrastructure.models import Ticket
from django.contrib.auth.models import User

class TicketDetailAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.ticket = Ticket.objects.create(title="Test Ticket", description="Test description", status="open", assigned_to=self.user)

    def test_get_ticket(self):
        response = self.client.get(f'/tickets/{self.ticket.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Ticket')

    def test_update_ticket(self):
        data = {'status': 'in_progress'}
        response = self.client.put(f'/tickets/{self.ticket.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ticket.refresh_from_db()
        self.assertEqual(self.ticket.status, 'in_progress')

    def test_delete_ticket(self):
        response = self.client.delete(f'/tickets/{self.ticket.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Ticket.objects.filter(id=self.ticket.id).exists())
