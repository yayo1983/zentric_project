from abc import ABC, abstractmethod
from products.domain.product_service import ProductService
from products.application.serializers import ProductSerializer
from products.infrastructure.product_repository_interfaces import ProductRepositoryInterface
from products.infrastructure.product_repository import ProductRepository

class AbstractFactory(ABC):
    @abstractmethod
    def create_service(self, product_repository: ProductRepositoryInterface) -> ProductService:
        pass

    @abstractmethod
    def create_serializer(self) -> ProductSerializer:
        pass
    
    @abstractmethod
    def create_repository(self) -> ProductRepository:
        pass

class ProductsFactory(AbstractFactory):
    
    
    def create_service(self, product_repository: ProductRepositoryInterface) -> ProductService:
        return ProductService(product_repository)


    def create_serializer(self) -> ProductSerializer:
        return ProductSerializer()
    
    
    def create_repository(self) -> ProductRepository:
        return ProductRepository()