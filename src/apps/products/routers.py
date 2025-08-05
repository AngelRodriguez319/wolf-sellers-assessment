from rest_framework.routers import SimpleRouter

from .views import ProductViewSet

PUBLIC_PRODUCT_ROUTER = SimpleRouter()
PUBLIC_PRODUCT_ROUTER.register("productos", ProductViewSet, basename="products")
