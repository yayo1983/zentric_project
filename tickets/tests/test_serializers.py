from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from tickets.infrastructure.models import Ticket
from tickets.application.serializers import TicketSerializer

class TicketSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        
        self.valid_data = {
            'title': 'Valid Ticket Title',
            'description': 'This is a valid description for the ticket.',
            'status': 'open',
            'assigned_to': self.user.id
        }
        self.invalid_data_status = {
            'title': 'Valid Ticket Title',
            'description': 'This is a valid description for the ticket.',
            'status': 'invalid_status',
            'assigned_to': self.user.id
        }

    def test_ticket_serializer_with_valid_data(self):
        serializer = TicketSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        ticket = serializer.save()
        self.assertEqual(ticket.title, self.valid_data['title'])
        self.assertEqual(ticket.description, self.valid_data['description'])
        self.assertEqual(ticket.status, self.valid_data['status'])
        self.assertEqual(ticket.assigned_to.id, self.valid_data['assigned_to'])

    def test_ticket_serializer_with_invalid_status(self):
        serializer = TicketSerializer(data=self.invalid_data_status)
        self.assertFalse(serializer.is_valid())
        self.assertIn('status', serializer.errors)

    # def test_ticket_serializer_missing_required_fields(self):
    #     invalid_data = {
    #         'title': '',
    #         'description': '',
    #         'status': '',
    #         'assigned_to': None
    #     }
    #     serializer = TicketSerializer(data=invalid_data)
    #     self.assertFalse(serializer.is_valid())
    #     self.assertIn('title', serializer.errors)
    #     self.assertIn('description', serializer.errors)
    #     self.assertIn('status', serializer.errors)
    #     self.assertIn('assigned_to', serializer.errors)
