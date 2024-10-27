# Generated by Django 4.2 on 2024-10-27 18:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('topic', models.CharField(max_length=128, verbose_name='Тема')),
                ('description', models.TextField(help_text='Минимальная длина 3 символа', validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Описание')),
                ('is_shown', models.BooleanField(default=True, verbose_name='Отображать')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_posts', to='posts.country', verbose_name='Страна')),
                ('tag', models.ManyToManyField(blank=True, null=True, related_name='tag_posts', to='posts.tag', verbose_name='Тег')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]