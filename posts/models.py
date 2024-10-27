from django.db import models

from accounts.models import CustomUser


class Country(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    alpha2Code = models.CharField(max_length=2, unique=True, verbose_name='Альфа 2 код')
    alpha3Code = models.CharField(max_length=3, unique=True, verbose_name='Альфа 3 код')
    capital = models.CharField(max_length=128, null=True, blank=True, verbose_name='Столица')
    region = models.CharField(max_length=64, null=True, blank=True, verbose_name='Регион')


    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
