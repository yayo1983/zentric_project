from rest_framework import serializers
from ..infrastructure.models import Product
from shareds.application.abstract_serializer import AbstractSerializer, CommonMetaClass


class ProductSerializer(AbstractSerializer, serializers.ModelSerializer, metaclass=CommonMetaClass):
    
    def get_serializer_class(self):
        return ProductSerializer
    
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'name': {'help_text': 'Name of the product'},
            'description': {'help_text': 'Description of the product'},
            'price': {'help_text': 'Price of the product'},
        }
        
        read_only_fields = ['created_at'] 
    
    def validate_name(self, value):
        """
            Validates that the name is not empty and has at least 3 characters.
        """
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value


    def validate_price(self, value):
        """
            Validates that the price is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser un valor positivo.")
        return value


    def validate(self, data):
        """
            Validates that expensive products are marked as premium.
        """
        if data['price'] > 1000 and 'premium' not in data['name'].lower():
            raise serializers.ValidationError("Productos con precio superior a 1000 deben incluir 'premium' en el nombre.")
        return data   
