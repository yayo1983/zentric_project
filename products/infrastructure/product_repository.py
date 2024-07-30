from products.infrastructure.models import Product
from products.infrastructure.interfaces.product_repository_interfaces import (
    ProductRepositoryInterface,
)


class ProductRepository(ProductRepositoryInterface):

    def get_all_products(self) -> dict:
        try:
            products = Product.objects.all()
            products_list = list(products.values())
            return products_list
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving products: {e}") from e

    def get_product_by_id(self, product_id) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving an product: {e}"
            ) from e
