import logging
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from notifications.abstract_factory import NotificationFactory, AbstractFactory

       
class BaseNotificationView:
        
    def __init__(self, factory: AbstractFactory = NotificationFactory()):
        self.factory = factory
        self.product_service = self.factory.create_service(self.factory.create_repository())
        self.serializer = self.factory.create_serializer()
        self.queryset = self.product_service.get_all()
        self.serializer_class = self.factory.create_serializer().get_serializer_class()
        self.permission_classes = [IsAuthenticated]
        self.logger = logging.getLogger(__name__)

class NotificationListCreateView(BaseNotificationView, generics.ListCreateAPIView):
    

    @swagger_auto_schema(
        operation_description="List all notifications",
        responses={200: 'NotificationSerializer(many=True)'}
    )
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while listing notifications: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Create a new notification",
        responses={201: 'NotificationSerializer'},
        request_body='NotificationSerializer'
    )
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while creating a notification: {e}", exc_info=True)
            raise
    
    def get_queryset(self):
        # Filter notifications by authenticated user
        return self.queryset.filter(recipient=self.request.user)

class NotificationRetrieveUpdateDestroyView(BaseNotificationView, generics.RetrieveUpdateDestroyAPIView):
    

    def get_queryset(self):
        # Filter notifications by authenticated user
        return self.queryset.filter(recipient=self.request.user)
    

class NotificationMarkAsReadView(BaseNotificationView, generics.RetrieveUpdateDestroyAPIView):
    

    def get_object(self):
        product_id = self.kwargs.get('pk')
        product = self.product_service.get_product_by_id(product_id)
        return product
    
   
    @swagger_auto_schema(
        operation_description="Retrieve a product by ID",
        responses={200: 'NotificationSerializer'}
    )
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while retrieving notification: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Update a notification by ID",
        responses={200: 'NotificationSerializer'},
        request_body='NotificationSerializer'
    )
    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while updating notification: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Partially update a notification by ID",
        responses={200: 'NotificationSerializer'},
        request_body='NotificationSerializer'
    )
    def patch(self, request, *args, **kwargs):
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while partially updating notification: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Delete a notification by ID",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while deleting notification: {e}", exc_info=True)
            raise
    
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.is_read = True
    #     instance.save()
    #     return super().update(request, *args, **kwargs)

