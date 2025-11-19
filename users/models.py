from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """класс для модели сотрудника"""

    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(
        max_length=15,
        verbose_name="телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
