from django.urls import include, path
from rest_framework.routers import SimpleRouter

from electronics_network.apps import ElectronicsNetworkConfig
from electronics_network.views import (ElectronicsNetworkViewSet,
                                       ProductViewSet, SupplierViewSet)

app_name = ElectronicsNetworkConfig.name

router = SimpleRouter()
router.register("products", ProductViewSet, basename="product")
router.register("suppliers", SupplierViewSet)
router.register("electronics-network", ElectronicsNetworkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
