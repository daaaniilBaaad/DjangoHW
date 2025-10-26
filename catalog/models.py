from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование", help_text="Введите наименование"
    )  # наименование,
    description = models.TextField(
        max_length=250, verbose_name="Описание", help_text="Введите описание"
    )  # описание,
    image = models.ImageField(
        upload_to="products/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )  # изображение,
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="категория",
        null=True,
        blank=True,
        related_name="products",
    )  # категория,
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена", help_text="Введите цену"
    )  # цена за покупку,
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания,
    updated_at = models.DateTimeField(auto_now=True)  # дата последнего изменения.

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category"]

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )  # наименование,
    description = models.TextField(
        max_length=250,
        verbose_name="Описание",
        help_text="Введите описание",
        blank=True,
        null=True,
    )  # описание.

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"
