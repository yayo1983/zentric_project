# schema.py

import graphene
from graphene_django.types import DjangoObjectType
from products.infrastructure.models import Product
from inventories.infrastructure.models import InventoryTransaction
from notifications.infrastructure.models import Notification
from tickets.infrastructure.models import Ticket

# Definition of data types
class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class InventoryType(DjangoObjectType):
    class Meta:
        model = InventoryTransaction

class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification

class TicketType(DjangoObjectType):
    class Meta:
        model = Ticket

# Definition of queries
class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_inventories = graphene.List(InventoryType)
    all_notifications = graphene.List(NotificationType)
    all_tickets = graphene.List(TicketType)

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_all_inventories(self, info, **kwargs):
        return InventoryTransaction.objects.all()

    def resolve_all_notifications(self, info, **kwargs):
        return Notification.objects.all()

    def resolve_all_tickets(self, info, **kwargs):
        return Ticket.objects.all()
        
    # Resolve for product by ID
    def resolve_product(self, info, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return None

# Schema Definition
schema = graphene.Schema(query=Query)
