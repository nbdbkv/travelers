# Generated by Django 4.2 on 2024-10-27 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/image', verbose_name='Фото')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_images', to='posts.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'фото поста',
                'verbose_name_plural': 'Фото поста',
            },
        ),
    ]
