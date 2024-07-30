import logging
from rest_framework.permissions import IsAuthenticated
from products.abstract_factory import ProductsFactory, AbstractFactory


class BaseSharedView:
        
    def __init__(self, factory: AbstractFactory = ProductsFactory()):
        self.factory = factory
        self.service = self.factory.create_service(self.factory.create_product_repository())
        self.serializer = self.factory.create_serializer()
        self.queryset = self.service.get_all_products()
        self.serializer_class = self.factory.create_serializer().get_serializer_class()
        self.permission_classes = [IsAuthenticated]
        self.logger = logging.getLogger(__name__)
        
        
    def get_queryset(self):
        return self.queryset

    def get_serializer_class(self):
        return self.serializer_class