from products.infrastructure.interfaces.product_repository_interfaces import ProductRepositoryInterface 
from products.infrastructure.models import Product


class ProductService:
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository
        

    def get_all_products(self) -> dict:
        try:
            return self.product_repository.get_all_products()
        except Exception as e:
            raise
    
    
    def get_product_by_id(self, product_id):
        try:
            return self.product_repository.get_product_by_id(product_id) 
        except Exception as e:
            raise