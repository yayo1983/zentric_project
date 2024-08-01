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

    def validate_total_inventory(self, product_id: int) -> int:
        try:
            total_incoming = self.inventory_repository.total_incoming(product_id)

            total_outgoing = self.inventory_repository.total_outgoing(product_id)
            total = total_incoming - total_outgoing
            if total >= 0:
                return total
            return -1
        except Exception as e:
            raise
