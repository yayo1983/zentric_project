from django.db import models
from rest_framework import serializers
from ..infrastructure.models import InventoryTransaction

class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = ['id', 'product', 'transaction_type', 'quantity', 'date']
        read_only_fields = ['date']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor que cero.")
        return value

    def validate(self, data):
        if data['transaction_type'] == 'exit':
            total_inventory = data['product'].inventory_set.aggregate(models.Sum('quantity'))['quantity__sum']
            if data['quantity'] > total_inventory:
                raise serializers.ValidationError("La cantidad para la transacción de salida no puede exceder el inventario total.")
        return data
