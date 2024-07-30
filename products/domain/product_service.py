from products.infrastructure.interfaces.product_repository_interfaces import ProductRepositoryInterface 
from products.infrastructure.models import Product


class ProductService:
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.Product_repository = product_repository
        

    def get_Product_abilities(self, name_id: str) -> Product:
        return self.Product_repository.get_Product_abilities(name_id)