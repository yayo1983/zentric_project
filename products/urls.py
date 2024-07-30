from django.urls import path
from products.application.views import ProductListCreate, ProductRetrieveUpdateDestroy


urlpatterns = [
    path('', ProductListCreate.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),

]
