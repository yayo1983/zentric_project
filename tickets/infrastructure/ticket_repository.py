from tickets.infrastructure.models import Ticket
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)


class TicketRepository(SharedRepositoryInterface):
    """
    Repository for managing Ticket data.

    This repository provides methods for retrieving tickets from the database. It includes functionality
    to retrieve all tickets and to retrieve a specific ticket by its ID.

    Methods:
    - get_all: Retrieve all tickets from the database.
    - get_by_id: Retrieve a specific ticket by its ID.
    """

    def get_all(self):
        """
        Retrieve all tickets from the database.

        This method fetches all Ticket objects, including related recipient data, from the database.
        If an error occurs during the retrieval, a ValueError is raised with an appropriate error message.

        Returns:
            QuerySet: A Django QuerySet containing all Ticket objects.

        Raises:
            ValueError: If an error occurs while retrieving the tickets.
        """
        try:
            return Ticket.objects.select_related("recipient").all().order_by("id")
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving tickets: {e}") from e

    def get_by_id(self, ticket_id: int) -> Ticket:
        """
        Retrieve a specific ticket by its ID.

        This method fetches a single Ticket object from the database based on the provided ID.
        If the ticket with the specified ID is not found or an error occurs during retrieval,
        a ValueError is raised with an appropriate error message.

        Args:
            ticket_id (int): The ID of the ticket to retrieve.

        Returns:
            Ticket: The Ticket object with the specified ID.

        Raises:
            ValueError: If the ticket with the specified ID is not found or an error occurs while retrieving it.
        """
        try:
            return Ticket.objects.get(id=ticket_id).order_by("id")
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving a Ticket: {e}") from e
