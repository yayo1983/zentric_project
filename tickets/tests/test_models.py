from django.test import TestCase
from django.contrib.auth.models import User
from tickets.infrastructure.models import Ticket

class TicketModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.ticket = Ticket.objects.create(
            title="Test Ticket",
            description="This is a test ticket.",
            status="open",
            assigned_to=self.user
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.title, "Test Ticket")
        self.assertEqual(self.ticket.description, "This is a test ticket.")
        self.assertEqual(self.ticket.status, "open")
        self.assertEqual(self.ticket.assigned_to, self.user)

    def test_ticket_string_representation(self):
        self.assertEqual(str(self.ticket), self.ticket.title)
