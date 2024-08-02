from django.test import TestCase
from django.contrib.auth.models import User
from inventories.infrastructure.models import InventoryTransaction
from products.infrastructure.models import Product


class InventoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=100.00,
            user=self.user,
        )
        self.inventory = InventoryTransaction.objects.create(
            product=self.product, quantity=10
        )

    def test_inventory_creation(self):
        self.assertEqual(self.inventory.product, self.product)
        self.assertEqual(self.inventory.quantity, 10)
