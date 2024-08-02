from django.db import models
from django.utils.translation import gettext_lazy as _
from products.infrastructure.models import Product

class InventoryTransaction(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    TRANSACTION_TYPES = [
        (IN, 'Ingreso'),
        (OUT, 'Salida'),
    ]
    ENTRY = 'entry', _('Entry')
    EXIT = 'exit', _('Exit')

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='inventory_transactions')
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.product.name} - {self.quantity}"