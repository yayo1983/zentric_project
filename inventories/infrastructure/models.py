from django.db import models
from django.utils.translation import gettext_lazy as _
from products.infrastructure.models import Product

class InventoryTransaction(models.Model):
    class TransactionType(models.TextChoices):
        ENTRY = 'entry', _('Entry')
        EXIT = 'exit', _('Exit')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_transactions')
    transaction_type = models.CharField(max_length=5, choices=TransactionType.choices)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.product.name} - {self.quantity}"

    def save(self, *args, **kwargs):
        if self.transaction_type == self.TransactionType.EXIT:
            total_inventory = self.product.inventory_transactions.aggregate(total_quantity=models.Sum('quantity'))['total_quantity']
            if total_inventory is None:
                total_inventory = 0

            if self.quantity > total_inventory:
                raise ValueError("La cantidad para la transacción de salida no puede exceder el inventario total.")

        super().save(*args, **kwargs)
