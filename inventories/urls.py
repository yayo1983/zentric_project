from django.urls import path
from inventories.application.views import (
    InventoryListCreateView,
    InventoryRetrieveUpdateDestroyView
)

urlpatterns = [
    path("", InventoryListCreateView.as_view(), name="inventory-list"),
    path(
        "<int:pk>/",
        InventoryRetrieveUpdateDestroyView.as_view(),
        name="inventory-detail",
    )
]
