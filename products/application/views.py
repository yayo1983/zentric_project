from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from products.infrastructure.models import Product
from products.application.serializers import ProductSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        operation_description="List all products",
        responses={200: ProductSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new product",
        responses={201: ProductSerializer},
        request_body=ProductSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a product by ID",
        responses={200: ProductSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a product by ID",
        responses={200: ProductSerializer},
        request_body=ProductSerializer
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partially update a product by ID",
        responses={200: ProductSerializer},
        request_body=ProductSerializer
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a product by ID",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
