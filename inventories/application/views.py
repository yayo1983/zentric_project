from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from inventories.inventory_factory import InventoryFactory
from shareds.application.view import BaseSharedView
from inventories.application.serializers import InventoryTransactionSerializer

class InventoryListCreateView(BaseSharedView, generics.ListCreateAPIView):
    """
    InventoryListCreateView handles listing and creating inventory records.
    Inherits from BaseSharedView and ListCreateAPIView.
    """

    def __init__(self):
        """
        Initialize the view with InventoryFactory and set up the view.
        """
        super().__init__(InventoryFactory())
        generics.ListCreateAPIView.__init__(self)

    @swagger_auto_schema(
        operation_description="List all inventories",
        responses={200: InventoryTransactionSerializer(many=True)},
    )
    @method_decorator(cache_page(60*15))  # Cache response for 15 minutes
    def get(self, request, *args, **kwargs):
        """
        Handle GET request to list all inventories.
        Caches the response for 15 minutes.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            # Log the error and re-raise the exception
            # self.logger.error(f"Error occurred while listing inventories: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Create a new inventory",
        responses={201: InventoryTransactionSerializer},
        request_body=InventoryTransactionSerializer,
    )
    def post(self, request, *args, **kwargs):
        """
        Handle POST request to create a new inventory.
        """
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            # Log the error and re-raise the exception
            # self.logger.error(f"Error occurred while creating an inventory: {e}", exc_info=True)
            raise

class InventoryRetrieveUpdateDestroyView(
    BaseSharedView, generics.RetrieveUpdateDestroyAPIView
):
    """
    InventoryRetrieveUpdateDestroyView handles retrieving, updating, and deleting inventory records.
    Inherits from BaseSharedView and RetrieveUpdateDestroyAPIView.
    """

    def __init__(self):
        """
        Initialize the view with InventoryFactory and set up the view.
        """
        super().__init__(InventoryFactory())
        generics.RetrieveUpdateDestroyAPIView.__init__(self)

    def get_object(self):
        """
        Retrieve a single inventory record by ID.
        Handles errors by logging and returning a response with an error message.
        """
        try:
            inventory_id = self.kwargs.get("pk")
            product = self.service.get_by_id(inventory_id)
            return product
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving inventory: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Retrieve an inventory by ID",
        responses={200: InventoryTransactionSerializer},
    )
    @method_decorator(cache_page(60*15))  # Cache response for 15 minutes
    def get(self, request, *args, **kwargs):
        """
        Handle GET request to retrieve an inventory by ID.
        Caches the response for 15 minutes.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving inventory: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update an inventory by ID",
        responses={200: InventoryTransactionSerializer},
        request_body=InventoryTransactionSerializer,
    )
    def put(self, request, *args, **kwargs):
        """
        Handle PUT request to update an inventory by ID.
        """
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while updating inventory: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an inventory by ID",
        responses={200: InventoryTransactionSerializer},
        request_body=InventoryTransactionSerializer,
    )
    def patch(self, request, *args, **kwargs):
        """
        Handle PATCH request to partially update an inventory by ID.
        """
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while partially updating inventory: {e}",
                exc_info=True,
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an inventory by ID",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request to delete an inventory by ID.
        """
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while deleting inventory: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
