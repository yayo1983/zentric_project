from tickets.domain.ticket_service import TicketService
from tickets.application.serializers import TicketSerializer
from shareds.infrastructure.shared_repository_interfaces import SharedRepositoryInterface
from tickets.infrastructure.ticket_repository import TicketRepository
from shareds.abstract_factory import AbstractFactory

class TicketFactory(AbstractFactory):
    
    
    def create_service(self, shared_repository: SharedRepositoryInterface) -> TicketService:
        return TicketService(shared_repository)


    def create_serializer(self) -> TicketSerializer:
        return TicketSerializer()
    
    
    def create_repository(self) -> TicketRepository:
        return TicketRepository()