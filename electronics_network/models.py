from django.db import models


class Product(models.Model):
    """Класс модели продукта"""
    name = models.CharField(max_length=255, verbose_name="название продукта")
    model = models.CharField(max_length=100, verbose_name="модель продукта")
    description = models.TextField(blank=True, null=True, verbose_name="описание продукта")
    release_date = models.DateField(verbose_name="дата выхода продукта на рынок")

    def __str__(self):
        """Функция строкового представления товара"""
        return f"{self.name}: модель - {self.model_number}, дата выпуска: {self.release_date}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Поставщики"


class Supplier(models.Model):
    """Класс модели поставщика"""
    name = models.CharField(max_length=255, verbose_name="название поставщика")
    email = models.EmailField(unique=True, verbose_name="email поставщика")
    country = models.CharField(max_length=255, verbose_name="страна поставщика")
    city = models.CharField(max_length=255, verbose_name="город поставщика")
    street = models.CharField(max_length=255, verbose_name="улица поставщика")
    house_number = models.CharField(max_length=255, verbose_name="номер дома поставщика")
    debt_to_supplier = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="задолженность перед поставщиком"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Функция строкового представления поставщика"""
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

class ElectronicsNetwork(models.Model):
    """Класс модели звена сети"""
    HIERARCHY_LEVELS = [
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Individual Enterpreneur'),
    ]
    name = models.CharField(max_length=255, verbose_name="название сети")
    contacts_email = models.EmailField(unique=True, verbose_name="email")
    contacts_country = models.CharField(max_length=255, verbose_name="страна")
    contacts_city = models.CharField(max_length=255, verbose_name="город")
    contacts_street = models.CharField(max_length=255, verbose_name="улица")
    contacts_house_number = models.CharField(max_length=255, verbose_name="номер дома")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="поставщик")
    level = models.IntegerField(choices=HIERARCHY_LEVELS, verbose_name="уровень иерархии сети")
    products = models.ManyToManyField(Product)
    debt_to_supplier = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="задолженность перед поставщиком"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Функция строкового представления звена сети"""
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
