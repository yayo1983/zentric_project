from products.infrastructure.models import Product
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)
from products.infrastructure.product_repository_interfaces import ProductRepositoryInterface


class ProductRepository(SharedRepositoryInterface, ProductRepositoryInterface):
    """
    Repository for managing Product data.

    This repository provides methods for retrieving product data from the database.
    It includes functionality to retrieve all products and to retrieve a specific product by its ID.

    Methods:
    - get_all: Retrieve all products from the database and return them as a list of dictionaries.
    - get_by_id: Retrieve a specific product by its ID.
    """

    def get_all(self) -> dict:
        """
        Retrieve all products from the database and return them as a list of dictionaries.

        This method fetches all Product objects from the database and converts them into a list of dictionaries.
        If an error occurs during retrieval, a ValueError is raised with an appropriate error message.

        Returns:
            dict: A list of dictionaries, where each dictionary represents a Product object.

        Raises:
            ValueError: If an error occurs while retrieving the products.
        """
        try:
            # Retrieve all Product objects
            products = Product.objects.all().order_by('id')
            # Convert the queryset to a list of dictionaries
            products_list = list(products.values())
            return products_list
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving products: {e}") from e

    def get_by_id(self, product_id: int) -> Product:
        """
        Retrieve a specific product by its ID.

        This method fetches a single Product object from the database based on the provided ID.
        If the product with the specified ID is not found or an error occurs during retrieval,
        a ValueError is raised with an appropriate error message.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The Product object with the specified ID.

        Raises:
            ValueError: If the product with the specified ID is not found or an error occurs while retrieving it.
        """
        try:
            return Product.objects.get(id=product_id)
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving a product: {e}"
            ) from e

    def filter_by_user_id(self, user_id: int):
        """
        Retrieve a list of products by user ID.

        This method fetches all  the Products object from the database based on the provided user ID.
        If the product with the specified ID is not found or an error occurs during retrieval,
        a ValueError is raised with an appropriate error message.

        Args:
            user_id (int): The ID of the product to retrieve.

        Returns:
            dict: A list of the Products object by the specified ID.

        Raises:
            ValueError: If pecifiednot found products with the user ID is not found or an error occurs while retrieving it.
        """
        try:
            return Product.objects.filter(user=user_id).order_by('id')
        except Exception as e:
            return Product.objects.none()