# Generated by Django 3.2.15 on 2022-11-23 06:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_actor', models.CharField(max_length=100, verbose_name='Имя')),
                ('age_actor', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description_actor', models.TextField(verbose_name='Описание')),
                ('image_actor', models.ImageField(upload_to='actors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Актеры и режиссеры',
                'verbose_name_plural': 'Актеры и режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=150, verbose_name='Категория')),
                ('description_category', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_genre', models.CharField(max_length=100, verbose_name='Имя')),
                ('description_genre', models.TextField(verbose_name='Описание')),
                ('url_genre', models.SlugField(max_length=160, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_movie', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline_movie', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description_movie', models.TextField(verbose_name='Описание')),
                ('poster_movie', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year_movie', models.PositiveSmallIntegerField(default=2019, verbose_name='Дата выхода')),
                ('country_movie', models.CharField(max_length=30, verbose_name='Страна')),
                ('world_premiere_movie', models.DateField(default=datetime.date.today, verbose_name='Премьера в мире')),
                ('budget_movie', models.PositiveIntegerField(default=0, help_text='указывать сумму в $$$', verbose_name='Бюджет')),
                ('fees_in_usa_movie', models.PositiveIntegerField(default=0, help_text='указывать сумму в $$$', verbose_name='Сборы в США')),
                ('fess_in_world_movie', models.PositiveIntegerField(default=0, help_text='указывать сумму в $$$', verbose_name='Сборы в мире')),
                ('url_movie', models.SlugField(max_length=130, unique=True, verbose_name='URL')),
                ('draft_movie', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors_movie', models.ManyToManyField(related_name='film_actor', to='mainapp.Actor', verbose_name='актеры')),
                ('category_movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.category', verbose_name='Категория')),
                ('directors_movie', models.ManyToManyField(related_name='film_director', to='mainapp.Actor', verbose_name='режиссер')),
                ('genres_movie', models.ManyToManyField(to='mainapp.Genre', verbose_name='жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_ratting_star', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
                'ordering': ['-value_ratting_star'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_review', models.EmailField(max_length=254)),
                ('name_review', models.CharField(max_length=100, verbose_name='Имя')),
                ('text_review', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('movie_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.movie', verbose_name='фильм')),
                ('parent_review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_rating', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('movie_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='mainapp.movie', verbose_name='фильм')),
                ('star_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_movie_short', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description_movie_short', models.TextField(verbose_name='Описание')),
                ('image_movie_short', models.ImageField(upload_to='movie_shots/', verbose_name='Изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Кадр из фильма',
                'verbose_name_plural': 'Кадры из фильма',
            },
        ),
    ]
