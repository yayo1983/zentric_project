from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..infrastructure.models import Ticket
from django.contrib.auth.models import User

class TicketAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.ticket = Ticket.objects.create(title="Test Ticket", description="Test description", status="open", assigned_to=self.user)

    def test_list_tickets(self):
        response = self.client.get('/tickets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_ticket(self):
        data = {
            'title': 'New Ticket',
            'description': 'New ticket description',
            'status': 'open',
            'assigned_to': self.user.id
        }
        response = self.client.post('/tickets/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 2)
