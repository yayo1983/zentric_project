from django.test import TestCase
from products.infrastructure.models import Product

class ProductModelTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=100.0)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 100.0)

    def test_product_string_representation(self):
        self.assertEqual(str(self.product), self.product.name)
