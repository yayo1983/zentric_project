from tickets.infrastructure.models import Ticket
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)


class TicketRepository(SharedRepositoryInterface):

    def get_all(self):
        try:
            return Ticket.objects.select_related('recipient').all()
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving tickets: {e}") from e

    def get_by_id(self, ticket_id: int) -> Ticket:
        try:
            return Ticket.objects.get(id=ticket_id)
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving an Ticket: {e}"
            ) from e
