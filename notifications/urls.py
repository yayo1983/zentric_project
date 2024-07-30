from django.urls import path
from notifications.application.views import NotificationListCreateView, NotificationRetrieveUpdateDestroyView, NotificationMarkAsReadView

urlpatterns = [
    path('', NotificationListCreateView.as_view(), name='notification-list'),
    path('<int:pk>/', NotificationRetrieveUpdateDestroyView.as_view(), name='notification-detail'),
    path('mark_as_read/<int:pk>/', NotificationMarkAsReadView.as_view(), name='mark_as_read'),
]
