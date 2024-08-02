import logging
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from shareds.abstract_factory import AbstractFactory
from shareds.domain.abstract_service import AbstractService
from rest_framework.pagination import PageNumberPagination
from django.conf import settings


class DynamicGroupPermission(BasePermission):
    def __init__(self, group_name=None, perm_code=None):
        self.group_name = group_name
        self.perm_code = perm_code

    def has_permission(self, request, view):
        user = request.user
        if user and self.group_name:
            has_group_permission = user.groups.filter(name=self.group_name).exists()
        else:
            has_group_permission = True

        if self.perm_code:
            has_perm = user.has_perm(self.perm_code)
        else:
            has_perm = True

        return has_group_permission and has_perm


class ProductPagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE
    page_size_query_param = "page_size"
    max_page_size = settings.MAX_PAGE_SIZE


class BaseSharedView:
    factory: AbstractFactory
    service: AbstractService

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
