from django.test import TestCase
from inventories.infrastructure.models import Inventory
from products.infrastructure.models import Product

class InventoryModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", description="A test product", price=100.00)
        self.inventory = Inventory.objects.create(product=self.product, quantity=10)

    def test_inventory_creation(self):
        self.assertEqual(self.inventory.product, self.product)
        self.assertEqual(self.inventory.quantity, 10)
