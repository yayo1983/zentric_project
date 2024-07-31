from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from tickets.ticket_factory import TicketFactory
from shareds.application.view import BaseSharedView

class TicketListCreateView(BaseSharedView, generics.ListCreateAPIView):
    def __init__(self):
        super().__init__(TicketFactory())
        generics.ListCreateAPIView.__init__(self)

    @swagger_auto_schema(
        operation_description="List all Tickets",
        responses={200: "TicketSerializer(many=True)"},
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            # self.logger.error(f"Error occurred while listing Tickets: {e}", exc_info=True)
            raise

    @swagger_auto_schema(
        operation_description="Create a new Ticket",
        responses={201: "TicketSerializer"},
        request_body="TicketSerializer",
    )
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            # self.logger.error(f"Error occurred while creating a Ticket: {e}", exc_info=True)
            raise


class TicketRetrieveUpdateDestroyView(
    BaseSharedView, generics.RetrieveUpdateDestroyAPIView
):
    def __init__(self):
        super().__init__(TicketFactory())
        generics.ListCreateAPIView.__init__(self)


    def get_object(self):
        try:
            ticket_id = self.kwargs.get("pk")
            ticket = self.service.get_by_id(ticket_id)
            return ticket
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving Ticket: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Retrieve a product by ID",
        responses={200: "TicketSerializer"},
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while retrieving Ticket: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update a Ticket by ID",
        responses={200: "TicketSerializer"},
        request_body="TicketSerializer",
    )
    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while updating Ticket: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Ticket by ID",
        responses={200: "TicketSerializer"},
        request_body="TicketSerializer",
    )
    def patch(self, request, *args, **kwargs):
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while partially updating Ticket: {e}",
                exc_info=True,
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Ticket by ID",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(
                f"Error occurred while deleting Ticket: {e}", exc_info=True
            )
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
