from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from products.product_factory import ProductsFactory
from shareds.application.view import BaseSharedView
from products.application.serializers import ProductSerializer


class ProductListCreate(BaseSharedView, generics.ListCreateAPIView):
    """
    View for listing and creating products.

    This view handles HTTP GET requests to list all products and HTTP POST requests to create a new
    product. It uses caching to optimize GET requests and includes error handling to log issues and
    provide meaningful responses.

    Methods:
    - get: List all products.
    - post: Create a new product.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the view with a product factory and ListCreateAPIView settings.

        Args:
            *args: Positional arguments for initialization.
            **kwargs: Keyword arguments for initialization.
        """
        super().__init__(ProductsFactory())
        generics.ListCreateAPIView.__init__(self, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="List all products",
        responses={200: ProductSerializer(many=True)}
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to list all products.

        This method retrieves a list of all products from the database, using caching to improve
        performance. It logs any errors encountered during the process and returns a 400 Bad Request
        response if an error occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the product list or an error message.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while listing products: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Create a new product",
        responses={201: ProductSerializer},
        request_body=ProductSerializer
    )
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new product.

        This method processes the creation of a new product, validating and saving the data. It logs
        any errors encountered during the process and returns a 400 Bad Request response if an error
        occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the created product or an error message.
        """
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while creating a product: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
class ProductRetrieveUpdateDestroy(BaseSharedView, generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single product.

    This view handles HTTP GET, PUT, PATCH, and DELETE requests for a single product. It includes
    error handling to log issues and provide meaningful responses.

    Methods:
    - get_object: Retrieve the product by ID.
    - get: Retrieve a product by ID.
    - put: Update a product by ID.
    - patch: Partially update a product by ID.
    - delete: Delete a product by ID.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the view with a product factory and RetrieveUpdateDestroyAPIView settings.

        Args:
            *args: Positional arguments for initialization.
            **kwargs: Keyword arguments for initialization.
        """
        super().__init__(ProductsFactory())
        generics.ListCreateAPIView.__init__(self, *args, **kwargs)

    def get_object(self):
        """
        Retrieve a product by its ID.

        This method fetches the product with the specified ID using the service layer. If an error
        occurs during the retrieval, it logs the error and returns a 400 Bad Request response.

        Returns:
            Product: The product with the specified ID.

        Raises:
            Response: A Django REST framework Response object with an error message if an error occurs.
        """
        try:
            product_id = self.kwargs.get('pk')
            product = self.service.get_by_id(product_id)
            return product
        except Exception as e:
            self.logger.error(f"Error occurred while retrieving product: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Retrieve a product by ID",
        responses={200: ProductSerializer}
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a product by its ID.

        This method retrieves a single product from the database based on the provided ID, using
        caching to optimize performance. It logs any errors encountered during the process and
        returns a 400 Bad Request response if an error occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the product or an error message.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while retrieving product: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update a product by ID",
        responses={200: ProductSerializer},
        request_body=ProductSerializer
    )
    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update a product by its ID.

        This method processes the update of a product based on the provided ID and request data.
        It logs any errors encountered during the update process and returns a 400 Bad Request
        response if an error occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the updated product or an error message.
        """
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while updating product: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a product by ID",
        responses={200: ProductSerializer},
        request_body=ProductSerializer
    )
    def patch(self, request, *args, **kwargs):
        """
        Handle PATCH requests to partially update a product by its ID.

        This method processes partial updates to a product based on the provided ID and request data.
        It logs any errors encountered during the process and returns a 400 Bad Request response if an
        error occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the partially updated product or an error message.
        """
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while partially updating product: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a product by ID",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete a product by its ID.

        This method processes the deletion of a product based on the provided ID. It logs any errors
        encountered during the deletion process and returns a 400 Bad Request response if an error
        occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with no content or an error message if an error occurs.
        """
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while deleting product: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

