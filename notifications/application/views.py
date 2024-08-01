from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from notifications.notification_factory import NotificationFactory
from shareds.application.view import BaseSharedView
from notifications.application.serializers import NotificationSerializer


class NotificationListCreateView(BaseSharedView, generics.ListCreateAPIView):
    """
    API view for listing and creating notifications.

    This view inherits from `BaseSharedView` and `ListCreateAPIView` to provide both listing
    and creation functionalities for notifications.

    Methods:
    - get: Handles GET requests to list all notifications. Uses caching for 15 minutes to
    improve performance.
    - post: Handles POST requests to create a new notification.
    """

    def __init__(self):
        """
        Initialize the view with the `NotificationFactory` and `ListCreateAPIView`.
        """
        super().__init__(NotificationFactory())
        generics.ListCreateAPIView.__init__(self)

    @swagger_auto_schema(
        operation_description="List all notifications",
        responses={200: NotificationSerializer(many=True)},
    )
    @method_decorator(cache_page(60 * 15))  # Cache response for 15 minutes
    def get(self, request, *args, **kwargs):
        """
        List all notifications.

        Retrieves all notifications and returns them in the response. The result is cached
        for 15 minutes to enhance performance.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response object with the list of notifications.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while listing notifications: {e}", exc_info=True
            )
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Create a new notification",
        responses={201: NotificationSerializer},
        request_body=NotificationSerializer,
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new notification.

        Processes the request to create a new notification and returns the created notification
        in the response.

        Args:
            request: The HTTP request object containing the notification data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response object with the created notification.
        """
        try:
            message = request.data.get("message", "")
            id_user_selected = request.data["recipient"]
            email = self.service.get_email_user(id_user_selected)
            result_sns = None
            response = super().post(request, *args, **kwargs)
            if email and response.status_code in {201, 200}:
                result_sns = self.service.publish_message_to_subscriber(email, message)
            if result_sns is not None:
                return response
            return Response(
                {"No se pudo enviar la notificación"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            self.logger.error(
                f"Error occurred while creating a notification: {e}", exc_info=True
            )
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class NotificationRetrieveUpdateDestroyView(
    BaseSharedView, generics.RetrieveUpdateDestroyAPIView
):
    """
    API view for retrieving, updating, and deleting a single notification.

    This view inherits from `BaseSharedView` and `RetrieveUpdateDestroyAPIView` to provide
    retrieval, updating, and deletion functionalities for a single notification.

    Methods:
    - get_object: Retrieves a notification by its ID.
    - get: Handles GET requests to retrieve a specific notification.
    - put: Handles PUT requests to update a specific notification.
    - patch: Handles PATCH requests to partially update a specific notification.
    - delete: Handles DELETE requests to delete a specific notification.
    """

    def __init__(self):
        """
        Initialize the view with the `NotificationFactory` and `RetrieveUpdateDestroyAPIView`.
        """
        super().__init__(NotificationFactory())
        generics.RetrieveUpdateDestroyAPIView.__init__(self)


class NotificationMarkAsReadView(BaseSharedView, generics.RetrieveUpdateDestroyAPIView):
    """
    API view for marking a notification as read.

    This view inherits from `BaseSharedView` and `RetrieveUpdateDestroyAPIView` to handle
    marking a notification as read and provides retrieval, updating, and deletion functionalities.

    Methods:
    - get_object: Retrieves a notification by its ID.
    - get: Handles GET requests to retrieve a specific notification.
    - put: Handles PUT requests to update a specific notification.
    - patch: Handles PATCH requests to partially update a specific notification.
    - delete: Handles DELETE requests to delete a specific notification.
    """

    def __init__(self, factory=NotificationFactory()):
        """
        Initialize the view with the `NotificationFactory` and `RetrieveUpdateDestroyAPIView`.

        Args:
            factory: An optional `NotificationFactory` instance for dependency injection.
        """
        super().__init__(factory)

    def get_object(self):
        """
        Retrieve a notification by its ID.

        This method attempts to fetch the notification using its ID. If the notification
        is not found, an error response is returned.

        Returns:
            The notification instance if found, otherwise an error response.
        """
        try:
            notification_id = self.kwargs.get("pk")
            notification = self.service.get_by_id(notification_id)
            return notification
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving notification: {e}", exc_info=True
            )
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Retrieve a notification by ID",
        responses={200: NotificationSerializer},
    )
    @method_decorator(cache_page(60 * 15))  # Cache response for 15 minutes
    def get(self, request, *args, **kwargs):
        """
        Retrieve a specific notification by ID.

        Retrieves the notification corresponding to the provided ID and returns it in the response.
        The result is cached for 15 minutes to enhance performance.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response object with the requested notification.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving notification: {e}", exc_info=True
            )
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update a notification by ID",
        responses={200: NotificationSerializer},
        request_body=NotificationSerializer,
    )
    def put(self, request, *args, **kwargs):
        """
        Update a specific notification by ID.

        Processes the request to update the notification corresponding to the provided ID and
        returns the updated notification in the response.

        Args:
            request: The HTTP request object containing the updated notification data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response object with the updated notification.
        """
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while updating notification: {e}", exc_info=True
            )
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a notification by ID",
        responses={200: NotificationSerializer},
        request_body=NotificationSerializer,
    )
    def patch(self, request, *args, **kwargs):
        """
        Partially update a specific notification by ID.

        Processes the request to partially update the notification corresponding to the provided ID
        and returns the updated notification in the response.

        Args:
            request: The HTTP request object containing the partial update data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response object with the partially updated notification.
        """
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while partially updating notification: {e}",
                exc_info=True,
            )
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a notification by ID",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific notification by ID.

        Processes the request to delete the notification corresponding to the provided ID.
        If successful, returns a no content response.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response object indicating successful deletion with no content.
        """
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while deleting notification: {e}", exc_info=True
            )
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
