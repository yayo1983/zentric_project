from django.test import TestCase
from .serializers import ProductSerializer
from .models import Product

class ProductSerializerTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=100.0)
        self.serializer = ProductSerializer(instance=self.product)

    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'price']))
        self.assertEqual(data['name'], 'Test Product')
        self.assertEqual(data['price'], '100.0')
