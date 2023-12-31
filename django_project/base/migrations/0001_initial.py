# Generated by Django 5.0 on 2023-12-29 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ім’я')),
                ('pen_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Псевдонім')),
                ('surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прізвище')),
                ('birthday_date', models.DateField(blank=True, null=True, verbose_name='Дата народження')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автори',
            },
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=255, verbose_name='Жанр')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Жанр книги',
                'verbose_name_plural': 'Жанри книг',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('description', models.TextField(blank=True, null=True)),
                ('page_count', models.PositiveIntegerField(verbose_name='Кількість сторінок')),
                ('language', models.CharField(max_length=128, verbose_name='Мова')),
                ('book_created_at', models.DateField(verbose_name='Дата написання книги')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.author', verbose_name='Автор')),
                ('book_genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.bookgenre', verbose_name='Жанр книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
