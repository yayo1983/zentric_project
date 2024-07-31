from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from tickets.ticket_factory import TicketFactory
from shareds.application.view import BaseSharedView
from tickets.application.serializers import TicketSerializer

class TicketListCreateView(BaseSharedView, generics.ListCreateAPIView):
    """
    View for listing and creating tickets.

    This view handles HTTP GET requests to list all tickets and HTTP POST requests to create a new
    ticket. It includes caching for GET requests and error handling for both listing and creation
    processes.

    Methods:
    - get: List all tickets.
    - post: Create a new ticket.
    """

    def __init__(self):
        """
        Initialize the view with a ticket factory and ListCreateAPIView settings.

        Args:
            *args: Positional arguments for initialization.
            **kwargs: Keyword arguments for initialization.
        """
        super().__init__(TicketFactory())
        generics.ListCreateAPIView.__init__(self)

    @swagger_auto_schema(
        operation_description="List all Tickets",
        responses={200: TicketSerializer(many=True)},
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to list all tickets.

        This method retrieves a list of all tickets from the database, applying caching to improve
        performance. It logs any errors encountered during the retrieval and raises an exception.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the list of tickets or an error message.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while listing Tickets: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Create a new Ticket",
        responses={201: TicketSerializer},
        request_body=TicketSerializer,
    )
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new ticket.

        This method processes the creation of a new ticket, including validation and saving of data.
        It logs any errors encountered during the creation and raises an exception.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the created ticket or an error message.
        """
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while creating a Ticket: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        

class TicketRetrieveUpdateDestroyView(BaseSharedView, generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single ticket.

    This view handles HTTP GET, PUT, PATCH, and DELETE requests for a single ticket. It includes
    methods for retrieving a ticket by ID, updating, partially updating, and deleting a ticket.
    It also includes error handling to log issues and provide meaningful responses.

    Methods:
    - get_object: Retrieve the ticket by ID.
    - get: Retrieve a ticket by ID.
    - put: Update a ticket by ID.
    - patch: Partially update a ticket by ID.
    - delete: Delete a ticket by ID.
    """

    def __init__(self):
        """
        Initialize the view with a ticket factory and RetrieveUpdateDestroyAPIView settings.

        Args:
            *args: Positional arguments for initialization.
            **kwargs: Keyword arguments for initialization.
        """
        super().__init__(TicketFactory())
        generics.ListCreateAPIView.__init__(self)

    def get_object(self):
        """
        Retrieve a ticket by its ID.

        This method fetches the ticket with the specified ID using the service layer. If an error
        occurs during retrieval, it logs the error and returns a 400 Bad Request response.

        Returns:
            Ticket: The ticket with the specified ID.

        Raises:
            Response: A Django REST framework Response object with an error message if an error occurs.
        """
        try:
            ticket_id = self.kwargs.get("pk")
            ticket = self.service.get_by_id(ticket_id)
            return ticket
        except Exception as e:
            self.logger.error(f"Error occurred while retrieving Ticket: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Retrieve a ticket by ID",
        responses={200: TicketSerializer},
    )
    @method_decorator(cache_page(60*15))  # Cache 15 mins
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a ticket by its ID.

        This method retrieves a single ticket from the database based on the provided ID, applying
        caching to optimize performance. It logs any errors encountered during retrieval and returns
        a 400 Bad Request response if an error occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the ticket or an error message.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while retrieving Ticket: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update a ticket by ID",
        responses={200: TicketSerializer},
        request_body=TicketSerializer,
    )
    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update a ticket by its ID.

        This method processes the update of a ticket based on the provided ID and request data.
        It logs any errors encountered during the update process and returns a 400 Bad Request
        response if an error occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the updated ticket or an error message.
        """
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while updating Ticket: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a ticket by ID",
        responses={200: TicketSerializer},
        request_body=TicketSerializer,
    )
    def patch(self, request, *args, **kwargs):
        """
        Handle PATCH requests to partially update a ticket by its ID.

        This method processes partial updates to a ticket based on the provided ID and request data.
        It logs any errors encountered during the process and returns a 400 Bad Request response if an
        error occurs.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Django REST framework Response object with the partially updated ticket or an error message.
        """
        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            self.logger.error(f"Error occurred while partially updating Ticket: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a ticket by ID",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete a ticket by its ID.

        This method processes the deletion of a ticket based on the provided ID. It logs any errors
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
            self.logger.error(f"Error occurred while deleting Ticket: {e}", exc_info=True)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

