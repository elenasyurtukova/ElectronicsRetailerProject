from rest_framework.viewsets import ModelViewSet
from electronics_network.models import Product, Supplier, ElectronicsNetwork
from electronics_network.serializers import ProductSerializer, SupplierSerializer, ElectronicsNetworkSerializer

class ProductViewSet(ModelViewSet):
    """Вьюсет для модели продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewSet(ModelViewSet):
    """Вьюсет для модели поставщика"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ElectronicsNetworkViewSet(ModelViewSet):
    """Вьюсет для модели звена сети"""
    queryset = ElectronicsNetwork.objects.all()
    serializer_class = ElectronicsNetworkSerializer
