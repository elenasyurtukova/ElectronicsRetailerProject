from django.urls import path, include
from rest_framework.routers import SimpleRouter

from electronics_network.apps import ElectronicsNetworkConfig
from electronics_network.views import (ProductViewSet, SupplierViewSet, ElectronicsNetworkViewSet)

app_name = ElectronicsNetworkConfig.name

router = SimpleRouter()
router.register("products", ProductViewSet)
router.register("suppliers", SupplierViewSet)
router.register("electronics-network", ElectronicsNetworkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
