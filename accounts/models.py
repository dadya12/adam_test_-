from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ('man', "Мужчина"),
        ('woman', "Женщина")
    ]
    user_information = models.TextField(null=True, blank=True, verbose_name='Информация о пользователе')
    phone_number = models.CharField(max_length=16, null=True, blank=True, verbose_name='номер телефона')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='пол')
