import logging
from rest_framework.permissions import IsAuthenticated
from shareds.abstract_factory import AbstractFactory


class BaseSharedView:
        
    def __init__(self, factory: AbstractFactory):
        self.factory = factory
        self.service = self.factory.create_service(self.factory.create_repository())
        self.serializer = self.factory.create_serializer()
        self.queryset = self.service.get_all()
        self.serializer_class = self.factory.create_serializer().get_serializer_class()
        self.permission_classes = [IsAuthenticated]
        self.logger = logging.getLogger(__name__)
        
        
    def get_queryset(self):
        return self.queryset

    def get_serializer_class(self):
        return self.serializer_class