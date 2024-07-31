from django.test import TestCase
from rest_framework.exceptions import ValidationError
from inventory.models import Product, Inventory
from inventory.serializers import InventorySerializer

class InventorySerializerTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", description="A test product", price=100.00)
        self.valid_data = {'product': self.product.id, 'quantity': 10}
        self.invalid_data = {'product': self.product.id, 'quantity': -5}

    def test_inventory_serializer_with_valid_data(self):
        serializer = InventorySerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_inventory_serializer_with_invalid_data(self):
        serializer = InventorySerializer(data=self.invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
