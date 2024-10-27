from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='Электронная почта')
    otp = models.CharField(max_length=6, null=True, blank=True, verbose_name='Код')
    can_post = models.BooleanField(default=True, verbose_name='Создать пост')
    has_access = models.BooleanField(default=True, verbose_name='Доступ')
    is_active = models.BooleanField(default=False, verbose_name='Активный')
    verify_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата верификации')

    username = None

    objects = CustomUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

