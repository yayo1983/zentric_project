from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group, Permission
from tickets.infrastructure.models import Ticket

class TicketListCreateViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        self.create_permissions()

        ticket_group = Group.objects.create(name="test group")
        add_ticket_permission = Permission.objects.get(codename="add_ticket")
        view_ticket_permission = Permission.objects.get(codename="view_ticket")
        edit_ticket_permission = Permission.objects.get(codename="edit_ticket")
        delete_ticket_permission = Permission.objects.get(codename="delete_ticket")
        ticket_group.permissions.add(
            add_ticket_permission,
            view_ticket_permission,
            edit_ticket_permission,
            delete_ticket_permission,
        )

        self.user.groups.add(ticket_group)
        
        
        self.client.force_authenticate(user=self.user)
        
        
        self.list_create_url = reverse('ticket-list-create')
        self.ticket = Ticket.objects.create(
            title="Test Ticket",
            description="This is a test ticket",
            status="open",
            assigned_to=self.user
        )
        
        
    def create_permissions(self):
        if not Permission.objects.filter(codename='add_ticket').exists():
            Permission.objects.create(
                codename='add_ticket',
                name='Can add ticket',
                content_type_id=Ticket._meta.app_label
            )
        if not Permission.objects.filter(codename='view_ticket').exists():
            Permission.objects.create(
                codename='view_ticket',
                name='Can view ticket',
                content_type_id=Ticket._meta.app_label
            )

    # def test_list_tickets(self):
    #     response = self.client.get(self.list_create_url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)  # Check if the created ticket is in the response

    # def test_create_ticket(self):
    #     data = {
    #         'title': 'New Ticket',
    #         'description': 'Description of the new ticket',
    #         'status': 'open',
    #         'assigned_to': self.user.id
    #     }
    #     response = self.client.post(self.list_create_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Ticket.objects.count(), 2)  # Check if a new ticket is created
    #     self.assertEqual(Ticket.objects.latest('id').title, 'New Ticket')

    # def test_create_ticket_unauthenticated(self):
    #     self.client.logout()
    #     data = {
    #         'title': 'New Ticket',
    #         'description': 'Description of the new ticket',
    #         'status': 'open',
    #         'assigned_to': self.user.id
    #     }
    #     response = self.client.post(self.list_create_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TicketRetrieveUpdateDestroyViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        
        self.create_permissions()

        ticket_group = Group.objects.create(name="test group")
        add_ticket_permission = Permission.objects.get(codename="add_ticket")
        view_ticket_permission = Permission.objects.get(codename="view_ticket")
        edit_ticket_permission = Permission.objects.get(codename="edit_ticket")
        delete_ticket_permission = Permission.objects.get(codename="delete_ticket")
        ticket_group.permissions.add(
            add_ticket_permission,
            view_ticket_permission,
            edit_ticket_permission,
            delete_ticket_permission,
        )

        self.user.groups.add(ticket_group)
        
        
        self.client.force_authenticate(user=self.user)
        
        self.ticket = Ticket.objects.create(
            title="Test Ticket",
            description="This is a test ticket",
            status="open",
            assigned_to=self.user
        )
        self.retrieve_update_destroy_url = reverse('ticket-detail', kwargs={'pk': self.ticket.id})
        
    
    def create_permissions(self):
        if not Permission.objects.filter(codename='add_ticket').exists():
            Permission.objects.create(
                codename='add_ticket',
                name='Can add ticket',
                content_type_id=Ticket._meta.app_label
            )
        if not Permission.objects.filter(codename='view_ticket').exists():
            Permission.objects.create(
                codename='view_ticket',
                name='Can view ticket',
                content_type_id=Ticket._meta.app_label
            )

    # def test_retrieve_ticket(self):
    #     response = self.client.get(self.retrieve_update_destroy_url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['title'], self.ticket.title)

