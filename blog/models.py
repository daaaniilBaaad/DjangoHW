from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog_previews/', blank=True, null=True, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published = models.BooleanField(default=False, verbose_name="Опубликовано")  # признак публикации
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Автор")

    class Meta:
        verbose_name = "Блог-пост"
        verbose_name_plural = "Блог-посты"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
