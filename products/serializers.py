from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'name': {'help_text': 'Name of the product'},
            'description': {'help_text': 'Description of the product'},
            'price': {'help_text': 'Price of the product'},
        }
