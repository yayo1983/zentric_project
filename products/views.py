from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from .models import Product
from .serializers import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(operation_description="Create a new product")
    def create(self, request, *args, **kwargs):
        """
        Create a new product.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a product by ID")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a product by ID.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update an existing product")
    def update(self, request, *args, **kwargs):
        """
        Update an existing product.
        """
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a product by ID")
    def destroy(self, request, *args, **kwargs):
        """
        Delete a product by ID.
        """
        return super().destroy(request, *args, **kwargs)
