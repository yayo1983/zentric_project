from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from inventories.infrastructure.models import Inventory
from products.infrastructure.models import Product

class InventoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Test Product", description="A test product", price=100.00)
        self.inventory = Inventory.objects.create(product=self.product, quantity=10)

    def test_list_inventories(self):
        response = self.client.get('/inventories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_inventory(self):
        data = {'product': self.product.id, 'quantity': 5}
        response = self.client.post('/inventories/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inventory.objects.count(), 2)
