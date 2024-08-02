from django.urls import path
from tickets.application.views import (
    TicketListCreateView,
    TicketRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('<int:pk>/', TicketRetrieveUpdateDestroyView.as_view(), name='ticket-detail'),
]
