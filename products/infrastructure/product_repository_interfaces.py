from abc import ABC, abstractmethod
from products.infrastructure.models import Product

class ProductRepositoryInterface(ABC):
    
    @abstractmethod
    def get_all(self) -> dict:
        pass
    
    @abstractmethod
    def get_by_id(self, product_id) -> Product:
        pass