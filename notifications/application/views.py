from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from notifications.notification_factory import NotificationFactory
from shareds.application.view import BaseSharedView

class NotificationListCreateView(BaseSharedView, generics.ListCreateAPIView):
    def __init__(self):
        super().__init__(NotificationFactory())
        generics.ListCreateAPIView.__init__(self)

    @swagger_auto_schema(
        operation_description="List all notifications",
        responses={200: "NotificationSerializer(many=True)"},
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            # self.logger.error(f"Error occurred while listing notifications: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Create a new notification",
        responses={201: "NotificationSerializer"},
        request_body="NotificationSerializer",
    )
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            # self.logger.error(f"Error occurred while creating a notification: {e}", exc_info=True)
            raise


class NotificationRetrieveUpdateDestroyView(
    BaseSharedView, generics.RetrieveUpdateDestroyAPIView
):
    def __init__(self):
        super().__init__(NotificationFactory())
        generics.ListCreateAPIView.__init__(self)


class NotificationMarkAsReadView(BaseSharedView, generics.RetrieveUpdateDestroyAPIView):
    def __init__(self, factory=NotificationFactory()):
        super().__init__(factory)

    def get_object(self):
        try:
            product_id = self.kwargs.get("pk")
            product = self.service.get_by_id(product_id)
            return product
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving notification: {e}", exc_info=True
            )
            raise

    @swagger_auto_schema(
        operation_description="Retrieve a product by ID",
        responses={200: "NotificationSerializer"},
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving notification: {e}", exc_info=True
            )
            raise

    @swagger_auto_schema(
        operation_description="Update a notification by ID",
        responses={200: "NotificationSerializer"},
        request_body="NotificationSerializer",
    )
    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while updating notification: {e}", exc_info=True
            )
            raise

    @swagger_auto_schema(
        operation_description="Partially update a notification by ID",
        responses={200: "NotificationSerializer"},
        request_body="NotificationSerializer",
    )
    def patch(self, request, *args, **kwargs):
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while partially updating notification: {e}",
                exc_info=True,
            )
            raise

    @swagger_auto_schema(
        operation_description="Delete a notification by ID",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while deleting notification: {e}", exc_info=True
            )
            raise
