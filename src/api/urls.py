from django.conf import settings
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from apps.products.routers import PUBLIC_PRODUCT_ROUTER

PUBLIC_API_V1_ROUTER = DefaultRouter()
PUBLIC_API_V1_ROUTER.registry.extend(PUBLIC_PRODUCT_ROUTER.registry)


schema_view = get_schema_view(
    openapi.Info(
        title=settings.PROJECT_NAME,
        default_version="v1",
        description="Documentación de la API para gestión de productos",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(PUBLIC_API_V1_ROUTER.urls)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
