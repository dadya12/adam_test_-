from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')

    def __str__(self):
        return self.name

class Ads(models.Model):
    STATUS_CHOICES = [
        ('moderated', 'На модерации'),
        ('published', 'Опубликовано'),
        ('on_delete', 'На удалении'),
        ('rejected', 'Отклонено')
    ]

    image = models.ImageField(upload_to='ads/picture/', null=True, blank=True, verbose_name='Фотография')
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), related_name='ads', on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, related_name='ads', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICES, default='moderated')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    published_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата ивремя публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')

class Comment(models.Model):
    text = models.TextField(max_length=200, verbose_name='Текст')
    author = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE, verbose_name='Автор')
    ads = models.ForeignKey(Ads, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
