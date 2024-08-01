from shareds.domain.abstract_service import AbstractService
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)
from products.infrastructure.models import Product
from products.domain.abstract_product_service import AbstractProductService

class ProductService(AbstractService, AbstractProductService):
    def __init__(self, product_repository: SharedRepositoryInterface):
        self.product_repository = product_repository

    def get_all(self) -> dict:
        try:
            return self.product_repository.get_all()
        except Exception as e:
            raise

    def get_by_id(self, product_id) -> Product:
        try:
            return self.product_repository.get_by_id(product_id)
        except Exception as e:
            raise

    def filter_by_user_id(self, user_id: int):
        try:
            return self.product_repository.filter_by_user_id(user_id)
        except Exception as e:
            raise
