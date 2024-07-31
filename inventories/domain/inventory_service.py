from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)
from inventories.infrastructure.models import InventoryTransaction
from shareds.domain.abstract_service import AbstractService


class InventoryService(AbstractService):
    def __init__(self, inventory_repository: SharedRepositoryInterface):
        self.inventory_repository = inventory_repository

    def get_all(self):
        try:
            return self.inventory_repository.get_all()
        except Exception as e:
            raise

    def get_by_id(self, inventory_id) -> InventoryTransaction:
        try:
            return self.inventory_repository.get_by_id(inventory_id)
        except Exception as e:
            raise
