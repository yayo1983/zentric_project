from django.contrib import admin
from products.infrastructure.models import Product

class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the product list in the admin panel
    list_display = ('name', 'price', 'created_at')

    # Searchable fields in the admin panel
    search_fields = ('name', 'description')

    # Filters in the admin panel sidebar
    list_filter = ('created_at',)
    
    # def has_add_permission(self, request):
    #     # Prevent adding notifications from the admin interface
    #     return False




# Register the model with the administrator settings
admin.site.register(Product, ProductAdmin)

