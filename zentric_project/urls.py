from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from graphene_django.views import GraphQLView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version="v1",
        description="API documentation for the Product app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('products/', include('products.urls')),
    path('notifications/', include('notifications.urls')),
    path('inventories/', include('inventories.urls')),
    path('tickets/', include('tickets.urls')),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(api_patterns)),
    path('graphql/', GraphQLView.as_view(graphiql=True)),  # `graphiql=True` Enables the graphical interface
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
