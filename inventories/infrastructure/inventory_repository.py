from inventories.infrastructure.models import InventoryTransaction
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)


class InventoryRepository(SharedRepositoryInterface):
    """
    Repository class for handling operations related to inventory transactions.

    This class implements methods to interact with the `InventoryTransaction` model, providing
    functionality to retrieve inventory transactions either as a list or by a specific ID. It extends
    from `SharedRepositoryInterface` to adhere to a shared repository contract.

    Methods:
    - get_all: Retrieves all inventory transactions from the database, including related product
      information.
    - get_by_id: Retrieves a specific inventory transaction by its ID.
    """

    def get_all(self):
        """
        Retrieve all inventory transactions from the database.

        This method fetches all inventory transaction records and their related product information
        using `select_related` for optimized querying. In case of an error during the retrieval
        process, a `ValueError` is raised with a descriptive message.

        Returns:
            QuerySet: A Django QuerySet containing all `InventoryTransaction` objects.

        Raises:
            ValueError: If an error occurs during the retrieval process.
        """
        try:
            return InventoryTransaction.objects.select_related('product').all()
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving inventory transactions: {e}") from e

    def get_by_id(self, inventory_id: int) -> InventoryTransaction:
        """
        Retrieve an inventory transaction by its ID.

        This method fetches a single `InventoryTransaction` record based on the provided ID. If the
        inventory transaction with the given ID does not exist or an error occurs during retrieval, a
        `ValueError` is raised with a descriptive message.

        Args:
            inventory_id (int): The ID of the inventory transaction to retrieve.

        Returns:
            InventoryTransaction: The `InventoryTransaction` object with the specified ID.

        Raises:
            ValueError: If the inventory transaction with the given ID does not exist or an error occurs
            during retrieval.
        """
        try:
            return InventoryTransaction.objects.get(id=inventory_id)
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving the inventory transaction: {e}"
            ) from e

