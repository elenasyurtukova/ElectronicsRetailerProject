from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("electronics_network/", include("electronics_network.urls", namespace="electronics_network")),
    path("users/", include("users.urls", namespace="users")),
]

