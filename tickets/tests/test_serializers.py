from django.test import TestCase
from rest_framework.exceptions import ValidationError
from tickets.application.serializers import TicketSerializer

class TicketSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'title': 'Test Ticket',
            'description': 'A description of the test ticket.',
            'status': 'open'
        }
        self.invalid_data = {
            'title': 'Invalid Ticket',
            'description': 'This ticket has an invalid status.',
            'status': 'invalid_status'
        }

    def test_ticket_serializer_with_valid_data(self):
        serializer = TicketSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_ticket_serializer_with_invalid_data(self):
        serializer = TicketSerializer(data=self.invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
