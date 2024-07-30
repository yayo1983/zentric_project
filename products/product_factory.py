from products.domain.product_service import ProductService
from products.application.serializers import ProductSerializer
from products.infrastructure.product_repository import ProductRepository
from shareds.abstract_factory import AbstractFactory
from shareds.infrastructure.shared_repository_interfaces import SharedRepositoryInterface


class ProductsFactory(AbstractFactory):
    
    
    def create_service(self, product_repository: SharedRepositoryInterface) -> ProductService:
        return ProductService(product_repository)


    def create_serializer(self) -> ProductSerializer:
        return ProductSerializer()
    
    
    def create_repository(self) -> ProductRepository:
        return ProductRepository()