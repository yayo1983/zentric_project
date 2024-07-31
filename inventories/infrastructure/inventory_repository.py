from inventories.infrastructure.models import InventoryTransaction
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)


class InventoryRepository(SharedRepositoryInterface):

    def get_all(self):
        try:
            return InventoryTransaction.objects.select_related('product').all()
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving products: {e}") from e

    def get_by_id(self, inventory_id: int) -> InventoryTransaction:
        try:
            return InventoryTransaction.objects.get(id=inventory_id)
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving an inventory: {e}"
            ) from e
