import logging
from rest_framework.permissions import IsAuthenticated
from shareds.abstract_factory import AbstractFactory
from rest_framework.pagination import PageNumberPagination
from django.conf import settings

class ProductPagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE  
    page_size_query_param = 'page_size'
    max_page_size = settings.MAX_PAGE_SIZE
    
    
class BaseSharedView:
        
    def __init__(self, factory: AbstractFactory):
        self.factory = factory
        self.service = self.factory.create_service(self.factory.create_repository())
        self.serializer = self.factory.create_serializer()
        self.queryset = self.service.get_all()
        self.serializer_class = self.factory.create_serializer().get_serializer_class()
        self.permission_classes = [IsAuthenticated]
        self.pagination_class = ProductPagination
        self.logger = logging.getLogger(__name__)
        
        
    def get_queryset(self):
        return self.queryset

    def get_serializer_class(self):
        return self.serializer_class