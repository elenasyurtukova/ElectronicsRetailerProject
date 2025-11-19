from itertools import product

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from electronics_network.models import Product, Supplier, ElectronicsNetwork
from users.models import User


class ProductTestCase(APITestCase):
    def setUp(self):
        """Функция подготовки данных перед тестированием"""
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("0147")
        self.client.force_authenticate(user=self.user)  # авторизуем пользователя
        self.product = Product.objects.create(
            name="холодильник1",
            model="testholod1",
            release_date="2020-01-01"
        )

    def test_product_create(self):
        """Тестирование создания экземпляра продукта"""
        url = reverse("electronics_network:product-list")
        data = {
            "name": "холодильник2",
            "model": "testholod2",
            "release_date": "2020-10-20",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.all().count(), 2)

    def test_product_list(self):
        """Тестирование запроса на вывод списка продуктов"""
        url = reverse("electronics_network:product-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.all().count(), 1)

    def test_product_detail(self):
        """Тестирование запроса на вывод полей продукта по заданному pk"""
        url = reverse("electronics_network:product-detail", args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "холодильник1")

    def test_product_update(self):
        """Тестирование запроса на изменение полей продукта"""
        url = reverse("electronics_network:product-detail", args=(self.product.pk,))
        data_update = {
            "name": "холодильник_1",
            "model": "testholod_1",
            "release_date": "2020-10-20",
        }
        response = self.client.put(url, data=data_update)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("release_date"), "2020-10-20")

    def test_product_delete(self):
        """Тестирование запроса на удаление продукта с заданным pk"""
        url = reverse("electronics_network:product-detail", kwargs={"pk": self.product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 0)


class SupplierTestCase(APITestCase):
    def setUp(self):
        """Функция подготовки данных перед тестированием"""
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("0147")
        self.client.force_authenticate(user=self.user)  # авторизуем пользователя
        self.supplier = Supplier.objects.create(
            name="поставщик1",
            email="supplier1@test.com",
            country="country1",
            city="city1",
            street="street1",
            house_number=1,
        )

    def test_supplier_create(self):
        """Тестирование создания экземпляра поставщика"""
        url = reverse("electronics_network:supplier-list")
        data = {
            "name": "поставщик2",
            "email": "supplier2@test.com",
            "country": "country2",
            "city": "city2",
            "street": "street2",
            "house_number": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.all().count(), 2)

    def test_supplier_list(self):
        """Тестирование запроса на вывод списка поставщиков"""
        url = reverse("electronics_network:supplier-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Supplier.objects.all().count(), 1)

    def test_supplier_detail(self):
        """Тестирование запроса на вывод полей поставщика по заданному pk"""
        url = reverse("electronics_network:supplier-detail", args=(self.supplier.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "supplier1@test.com")

    def test_supplier_update(self):
        """Тестирование запроса на изменение полей поставщика"""
        url = reverse("electronics_network:supplier-detail", args=(self.supplier.pk,))
        data_update = {
            "name": "поставщик_1",
            "email": "supplier_1@test.com",
            "country": "country_1",
            "city": "city_1",
            "street": "street_1",
            "house_number": 1,
            "debt_to_supplier": 10
        }
        response = self.client.put(url, data=data_update)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("city"), "city_1")
        self.assertEqual(data.get("debt_to_supplier"), "0.00")

    def test_supplier_delete(self):
        """Тестирование запроса на удаление поставщика с заданным pk"""
        url = reverse("electronics_network:supplier-detail", kwargs={"pk": self.supplier.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.all().count(), 0)

class ElectronicsNetworkTestCase(APITestCase):

    def setUp(self):
        """Функция подготовки данных перед тестированием"""
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("0147")
        self.client.force_authenticate(user=self.user)  # авторизуем пользователя
        self.supplier = Supplier.objects.create(
            name="поставщик1",
            email="supplier1@test.com",
            country="country1",
            city="city1",
            street="street1",
            house_number=1, )
        self.supplier_2 = Supplier.objects.create(
            name="поставщик2",
            email="supplier2@test.com",
            country="country2",
            city="city2",
            street="street2",
            house_number=2, )
        self.product1 = Product.objects.create(
            name="холодильник_1",
            model="testholod_1",
            release_date="2021-01-01"
        )
        self.product2 = Product.objects.create(
            name="холодильник_2",
            model="testholod_2",
            release_date="2022-01-01"
        )
        self.product3 = Product.objects.create(
            name="холодильник_3",
            model="testholod_3",
            release_date="2023-01-01"
        )


    def test_electronics_network_create(self, products=None):
        """Тестирование создания экземпляра звена сети"""
        url = reverse("electronics_network:electronicsnetwork-list")
        data = {
            "name": "звено_сети_1",
            "contacts_email": "network1@test.com",
            "contacts_country": "country1",
            "contacts_city": "city1",
            "contacts_street": "street1",
            "contacts_house_number": 1,
            "supplier": self.supplier.id,
            "level": 0,
            "products": [self.product1.id, self.product2.id],
            "debt_to_supplier": 50000
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ElectronicsNetwork.objects.all().count(), 1)
        created_object = ElectronicsNetwork.objects.get(pk=response.data['id'])
        related_objects_ids = list(created_object.products.values_list('id', flat=True))
        self.assertCountEqual(related_objects_ids, [self.product1.id, self.product2.id])

    def test_electronics_network_list(self):
        """Тестирование запроса на вывод списка звеньев сети"""
        url = reverse("electronics_network:electronicsnetwork-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ElectronicsNetwork.objects.all().count(), 0)

    def test_electronics_network_detail(self):
        """Тестирование запроса на вывод полей звена сети по заданному pk"""
        data = {
            "name": "звено_сети_2",
            "contacts_email": "network2@test.com",
            "contacts_country": "country2",
            "contacts_city": "city2",
            "contacts_street": "street2",
            "contacts_house_number": 2,
            "supplier": self.supplier_2.id,
            "level": 1,
            "products": [self.product1.id, self.product3.id],
            "debt_to_supplier": 100000
        }
        url_create = reverse("electronics_network:electronicsnetwork-list")
        response = self.client.post(url_create, data)
        data_create = response.json()
        url = reverse("electronics_network:electronicsnetwork-detail", args=(data_create['id'],))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["contacts_email"], "network2@test.com")

    def test_electronics_network_update(self):
        """Тестирование запроса на изменение полей звена сети"""
        data = {
            "name": "звено_сети_2",
            "contacts_email": "network2@test.com",
            "contacts_country": "country2",
            "contacts_city": "city2",
            "contacts_street": "street2",
            "contacts_house_number": 2,
            "supplier": self.supplier_2.id,
            "level": 1,
            "products": [self.product1.id, self.product2.id],
            "debt_to_supplier": 50000
        }
        url_create = reverse("electronics_network:electronicsnetwork-list")
        response = self.client.post(url_create, data)
        data_create = response.json()
        url = reverse("electronics_network:electronicsnetwork-detail", args=(data_create['id'],))
        data_update = {
            "name": "звено_сети2",
            "contacts_email": "network2@test.com",
            "contacts_country": "country2",
            "contacts_city": "city_2",
            "contacts_street": "street2",
            "contacts_house_number": 2,
            "supplier": self.supplier_2.id,
            "level": 1,
            "products": [self.product1.id, self.product2.id],
            "debt_to_supplier": 150000
        }
        response = self.client.put(url, data=data_update)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("contacts_city"), "city_2")
        self.assertEqual(data.get("debt_to_supplier"), "150000.00")

    def test_electronics_network_delete(self):
        """Тестирование запроса на удаление звена сети с заданным pk"""
        data = {
            "name": "звено_сети_2",
            "contacts_email": "network2@test.com",
            "contacts_country": "country2",
            "contacts_city": "city2",
            "contacts_street": "street2",
            "contacts_house_number": 2,
            "supplier": self.supplier_2.id,
            "level": 1,
            "products": [self.product1.id, self.product2.id],
            "debt_to_supplier": 50000
        }
        url_create = reverse("electronics_network:electronicsnetwork-list")
        response = self.client.post(url_create, data)
        data_create = response.json()
        url = reverse("electronics_network:electronicsnetwork-detail", args=(data_create['id'],))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.all().count(), 2)
