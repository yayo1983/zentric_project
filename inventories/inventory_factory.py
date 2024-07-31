from inventories.domain.inventory_service import InventoryService
from inventories.application.serializers import InventoryTransactionSerializer
from shareds.infrastructure.shared_repository_interfaces import SharedRepositoryInterface
from inventories.infrastructure.inventory_repository import InventoryRepository
from shareds.abstract_factory import AbstractFactory

class InventoryFactory(AbstractFactory):
    
    
    def create_service(self, shared_repository: SharedRepositoryInterface) -> InventoryService:
        return InventoryService(shared_repository)


    def create_serializer(self) -> InventoryTransactionSerializer:
        return InventoryTransactionSerializer()
    
    
    def create_repository(self) -> InventoryRepository:
        return InventoryRepository()