from django.urls import path
from products.application.views import ProductListCreate, ProductRetrieveUpdateDestroy


urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),

]
