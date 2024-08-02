from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group, Permission
from inventories.infrastructure.models import InventoryTransaction
from products.infrastructure.models import Product

class InventoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="12345")
        
        self.create_permissions()

        product_group = Group.objects.create(name="test group")
        add_inventory_permission = Permission.objects.get(codename="add_inventory")
        view_inventory_permission = Permission.objects.get(codename="view_inventory")
        edit_inventory_permission = Permission.objects.get(codename="edit_inventory")
        delete_inventory_permission = Permission.objects.get(codename="delete_inventory")
        product_group.permissions.add(
            add_inventory_permission,
            view_inventory_permission,
            edit_inventory_permission,
            delete_inventory_permission,
        )
        
        self.client.force_authenticate(user=self.user)

        
        self.product = Product.objects.create(name="Test Product", description="A test product", price=100.00)
        self.inventory = InventoryTransaction.objects.create(product=self.product, quantity=10)
        
    def create_permissions(self):
        if not Permission.objects.filter(codename='add_inventory').exists():
            Permission.objects.create(
                codename='add_inventory',
                name='Can add inventory',
                content_type_id=Product._meta.app_label
            )
        if not Permission.objects.filter(codename='view_inventory').exists():
            Permission.objects.create(
                codename='view_inventory',
                name='Can view inventory',
                content_type_id=Product._meta.app_label
            )

    # def test_list_inventories(self):
    #     response = self.client.get('/inventories/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)

    # def test_create_inventory(self):
    #     data = {'product': self.product.id, 'quantity': 5}
    #     response = self.client.post('/inventories/', data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(InventoryTransaction.objects.count(), 2)
