from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from electronics_network.models import Product, Supplier, ElectronicsNetwork


class ProductSerializer(ModelSerializer):
    """Класс сериализатора для модели продукта"""

    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(ModelSerializer):
    """Класс сериализатора для модели поставщика"""

    class Meta:
        model = Supplier
        fields = "__all__"

    def update(self, instance, validated_data):
        """функция, исключающая обновление поля задолженности у объекта поставщика"""
        validated_data.pop("debt_to_supplier", None)
        return super().update(instance, validated_data)


class ElectronicsNetworkSerializer(ModelSerializer):
    """Класс сериализатора для модели звена сети"""

    class Meta:
        model = ElectronicsNetwork
        fields = "__all__"
