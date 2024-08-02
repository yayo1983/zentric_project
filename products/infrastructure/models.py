from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Relation with the user
    name = models.CharField(max_length=255, unique=True, help_text="Name of the product")
    description = models.TextField(help_text="Description of the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the product")
    reorder_level = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Creation timestamp")
    updated_at = models.DateTimeField(auto_now=True, help_text="Last update timestamp")
    
    # class Meta:
        # permissions = [
        #     ("add_product", "Can add product"),
        #     ("view_product", "Can view product"),
        #     ("edit_product", "Can edit product"),
        #     ("delete_product", "Can delete product"),
        # ]

    def __str__(self):
        return self.name
