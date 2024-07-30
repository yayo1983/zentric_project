from products.infrastructure.models import Product
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)


class ProductRepository(SharedRepositoryInterface):

    def get_all(self) -> dict:
        try:
            products = Product.objects.all()
            products_list = list(products.values())
            return products_list
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving products: {e}") from e

    def get_by_id(self, product_id) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving an product: {e}"
            ) from e
