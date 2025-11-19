from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from electronics_network.models import ElectronicsNetwork, Product, Supplier
from electronics_network.serializers import (ElectronicsNetworkSerializer,
                                             ProductSerializer,
                                             SupplierSerializer)
from users.permissions import IsActive


class ProductViewSet(ModelViewSet):
    """Вьюсет для модели продукта"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsActive)


class SupplierViewSet(ModelViewSet):
    """Вьюсет для модели поставщика"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, IsActive)

    def get_queryset(self):
        """Метод поиска поставщика по стране из URL"""
        queryset = Supplier.objects.all()  # получаем все объекты

        # Получаем параметры из URL
        country = self.request.query_params.get("country", None)

        # Применяем фильтры, если параметры присутствуют
        if country:
            queryset = queryset.filter(country__icontains=country)
        return queryset


class ElectronicsNetworkViewSet(ModelViewSet):
    """Вьюсет для модели звена сети"""

    queryset = ElectronicsNetwork.objects.all()
    serializer_class = ElectronicsNetworkSerializer
    permission_classes = (IsAuthenticated, IsActive)

    def get_queryset(self):
        """Метод поиска звена сети по стране из URL"""
        queryset = ElectronicsNetwork.objects.all()  # получаем все объекты

        # Получаем параметры из URL
        contacts_country = self.request.query_params.get("contacts_country", None)

        # Применяем фильтры, если параметры присутствуют
        if contacts_country:
            queryset = queryset.filter(contacts_country__icontains=contacts_country)
        return queryset
