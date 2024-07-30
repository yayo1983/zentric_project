from notifications.domain.notification_service import NotificationService
from notifications.application.serializers import NotificationSerializer
from shareds.infrastructure.shared_repository_interfaces import SharedRepositoryInterface
from products.infrastructure.product_repository import ProductRepository
from shareds.abstract_factory import AbstractFactory

class NotificationFactory(AbstractFactory):
    
    
    def create_service(self, shared_repository: SharedRepositoryInterface) -> NotificationService:
        return NotificationService(shared_repository)


    def create_serializer(self) -> NotificationSerializer:
        return NotificationSerializer()
    
    
    def create_repository(self) -> ProductRepository:
        return ProductRepository()