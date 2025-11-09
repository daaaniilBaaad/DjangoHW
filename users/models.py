from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(max_length=15, verbose_name="Телефон", null=True, blank=True, help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Аватар", null=True, blank=True, help_text="Загрузите ваше фото")
    country = models.CharField(max_length=100, verbose_name="Страна", null=True, blank=True, help_text="Введите название вашей страны")

    token = models.CharField(max_length=100, verbose_name="Токен", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email