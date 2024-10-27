from django.core.validators import MinLengthValidator
from django.db import models

from accounts.models import CustomUser


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


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


class Post(TimeStampedModel):
    topic = models.CharField(max_length=128, verbose_name='Тема')
    description = models.TextField(
        validators=[MinLengthValidator(3)], help_text='Минимальная длина 3 символа', verbose_name='Описание',
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='user_posts', verbose_name='Пользователь',
    )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_posts', verbose_name='Страна')
    tag = models.ManyToManyField(Tag, null=True, blank=True, related_name='tag_posts', verbose_name='Тег')
    is_shown = models.BooleanField(default=True, verbose_name='Отображать')

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.user.email} - {self.topic}'
