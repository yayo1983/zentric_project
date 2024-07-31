from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from inventories.inventory_factory import InventoryFactory
from shareds.application.view import BaseSharedView

class InventoryListCreateView(BaseSharedView, generics.ListCreateAPIView):
    def __init__(self):
        super().__init__(InventoryFactory())
        generics.ListCreateAPIView.__init__(self)

    @swagger_auto_schema(
        operation_description="List all inventories",
        responses={200: "InventorySerializer(many=True)"},
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            # self.logger.error(f"Error occurred while listing inventories: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Create a new inventory",
        responses={201: "InventorySerializer"},
        request_body="InventorySerializer",
    )
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            # self.logger.error(f"Error occurred while creating a inventory: {e}", exc_info=True)
            raise


class InventoryRetrieveUpdateDestroyView(
    BaseSharedView, generics.RetrieveUpdateDestroyAPIView
):
    def __init__(self):
        super().__init__(InventoryFactory())
        generics.ListCreateAPIView.__init__(self)


    def get_object(self):
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
        operation_description="Retrieve a product by ID",
        responses={200: "InventorySerializer"},
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving inventory: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update a inventory by ID",
        responses={200: "InventorySerializer"},
        request_body="InventorySerializer",
    )
    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while updating inventory: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a inventory by ID",
        responses={200: "InventorySerializer"},
        request_body="InventorySerializer",
    )
    def patch(self, request, *args, **kwargs):
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while partially updating inventory: {e}",
                exc_info=True,
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a inventory by ID",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while deleting inventory: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
