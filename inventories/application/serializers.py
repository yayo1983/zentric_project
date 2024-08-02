from django.db import models
from rest_framework import serializers
from ..infrastructure.models import InventoryTransaction
from shareds.application.abstract_serializer import AbstractSerializer, CommonMetaClass
from products.infrastructure.models import Product

# The `InventoryTransactionSerializer` class is a serializer class in Django used for serializing and
# deserializing instances of the `InventoryTransaction` model. It extends `AbstractSerializer` and
# `serializers.ModelSerializer` and is defined with a metaclass `CommonMetaClass`.
class InventoryTransactionSerializer(AbstractSerializer, serializers.ModelSerializer, metaclass=CommonMetaClass):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()
    
    def get_serializer_class(self):
        return InventoryTransactionSerializer
    class Meta:
        model = InventoryTransaction
        fields = ['id', 'product', 'transaction_type', 'quantity', 'date']
        read_only_fields = ['date']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor que cero.")
        return value

    def validate(self, data):
        if data['transaction_type'] == 'OUT':
            from inventories.inventory_factory import InventoryFactory
            factory = InventoryFactory()
            inventory_service = factory.create_service(factory.create_repository())
            total_inventory = inventory_service.validate_total_inventory(data['product'].id)
            if data['quantity'] > total_inventory:
                raise serializers.ValidationError("La cantidad para la transacción de salida no puede exceder el inventario total.")
            if data['product'].reorder_level <= total_inventory:
                message = "Se necesita resurtir el producto "+ data['product'].name
                print(message)
                
        return data
