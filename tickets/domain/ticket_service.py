from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)
from tickets.infrastructure.models import Ticket
from shareds.domain.abstract_service import AbstractService


class TicketService(AbstractService):
    def __init__(self, ticket_repository: SharedRepositoryInterface):
        self.ticket_repository = ticket_repository

    def get_all(self):
        try:
            return self.ticket_repository.get_all()
        except Exception as e:
            raise

    def get_by_id(self, ticket_id) -> Ticket:
        try:
            return self.ticket_repository.get_by_id(ticket_id)
        except Exception as e:
            raise
