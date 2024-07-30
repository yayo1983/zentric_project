from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from products.product_factory import ProductsFactory
from shareds.application.view import BaseSharedView


class ProductListCreate(BaseSharedView, generics.ListCreateAPIView):
    def __init__(self, *args, **kwargs):
        super().__init__(ProductsFactory())
        generics.ListCreateAPIView.__init__(self, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="List all products",
        responses={200: 'ProductSerializer(many=True)'}
    )
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while listing products: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Create a new product",
        responses={201: 'ProductSerializer'},
        request_body='ProductSerializer'
    )
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while creating a product: {e}", exc_info=True)
            raise

class ProductRetrieveUpdateDestroy(BaseSharedView, generics.RetrieveUpdateDestroyAPIView):
    def __init__(self, *args, **kwargs):
        super().__init__(ProductsFactory())
        generics.ListCreateAPIView.__init__(self, *args, **kwargs)


    def get_object(self):
        product_id = self.kwargs.get('pk')
        product = self.service.get_by_id(product_id)
        return product
    
   
    @swagger_auto_schema(
        operation_description="Retrieve a product by ID",
        responses={200: 'ProductSerializer'}
    )
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while retrieving product: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Update a product by ID",
        responses={200: 'ProductSerializer'},
        request_body='ProductSerializer'
    )
    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while updating product: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Partially update a product by ID",
        responses={200: 'ProductSerializer'},
        request_body='ProductSerializer'
    )
    def patch(self, request, *args, **kwargs):
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while partially updating product: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Delete a product by ID",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while deleting product: {e}", exc_info=True)
            raise
