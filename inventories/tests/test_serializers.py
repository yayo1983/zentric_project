from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from inventories.infrastructure.models import Product
from inventories.application.serializers import InventoryTransactionSerializer


class InventorySerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=100.00,
            user=self.user,
        )
        self.valid_data = {
            "product": self.product.id,
            "quantity": 10,
            "transaction_type": "IN",  
        }
        self.invalid_data = {
            "product": self.product.id,
            "quantity": -5,
            "transaction_type": "OUT",  
        }

    def test_inventory_serializer_with_valid_data(self):
        serializer = InventoryTransactionSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_inventory_serializer_with_invalid_data(self):
        serializer = InventoryTransactionSerializer(data=self.invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
