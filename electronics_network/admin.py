from django.contrib import admin

from electronics_network.models import Product, Supplier, ElectronicsNetwork


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "description", "release_date")
    list_filter = ("name",)
    search_fields = ("name", "release_date")


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "country", "city", "street", "house_number", "debt_to_supplier", "created_at")
    list_filter = ("name", "email", "country", "city")
    search_fields = ("name", "email",)


@admin.register(ElectronicsNetwork)
class ElectronicsNetworkAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts_email", "contacts_country", "contacts_city", "contacts_street",
                    "contacts_house_number", "supplier", "level", "products", "debt_to_supplier", "created_at")
    list_filter = ("contacts_city", )
    search_fields = ("name", )

