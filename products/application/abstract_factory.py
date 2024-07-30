from abc import ABC, abstractmethod
from products.domain import ProductService
from products.application.serializers import ProductSerializer
from products.infrastructure.Products_repository import ProductsRepository
from products.infrastructure.models import Product


class ServiceFactory(ABC):
    @abstractmethod
    def create_service(self) -> ProductService:
        pass

    @abstractmethod
    def create_serializer(self, products: Product) -> ProductSerializer:
        pass
    
    @abstractmethod
    def create_products_repository(self):
        pass

class ProductsFactory(ServiceFactory):
    def create_service(self) -> ProductService:
        return ProductService(self.create_Products_repository())

    def create_serializer(self, products: Product) -> ProductSerializer:
        return ProductSerializer(Product)
    
    def create_Products_repository(self):
        return ProductRepository()