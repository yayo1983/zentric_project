from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductView

router = DefaultRouter()
router.register(r'products', ProductView)

urlpatterns = [
    path('', include(router.urls)),
]
