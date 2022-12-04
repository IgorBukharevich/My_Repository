from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    """Model 'Category'"""
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    name_category = models.CharField(
        verbose_name=u'Категория',
        max_length=150,
    )

    description_category = models.TextField(
        verbose_name=u'Описание'
    )

    url = models.SlugField(
        verbose_name=u'URL',
        max_length=160,
        unique=True,
    )

    def __str__(self):
        return self.name_category


class Actor(models.Model):
    """Model 'Actor'"""
    class Meta:
        verbose_name = u'Актеры и режиссеры'
        verbose_name_plural = u'Актеры и режиссеры'

    name_actor = models.CharField(
        verbose_name=u'Имя',
        max_length=100,
    )

    age_actor = models.PositiveSmallIntegerField(
        verbose_name=u'Возраст',
        default=0,
    )

    description_actor = models.TextField(
        verbose_name=u'Описание',
    )

    image_actor = models.ImageField(
        verbose_name=u'Изображение',
        upload_to="actors/",
        blank=True,
    )

    def __str__(self):
        return self.name_actor

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name_actor})


class Genre(models.Model):
    """Model 'Genre'"""
    class Meta:
        verbose_name = u'Жанр'
        verbose_name_plural = u'Жанры'

    name_genre = models.CharField(
        verbose_name=u'Имя',
        max_length=100,
    )

    description_genre = models.TextField(
        verbose_name=u'Описание',
    )

    url_genre = models.SlugField(
        verbose_name=u'URL',
        max_length=160,
        unique=True,
    )

    def __str__(self):
        return self.name_genre


class Movie(models.Model):
    """Model 'Movie'"""
    class Meta:
        verbose_name = u'Фильм'
        verbose_name_plural = u'Фильмы'

    title_movie = models.CharField(
        verbose_name=u'Название',
        max_length=100,
    )

    tagline_movie = models.CharField(
        verbose_name=u'Слоган',
        max_length=100,
        default='',
    )

    description_movie = models.TextField(
        verbose_name=u'Описание',
    )

    poster_movie = models.ImageField(
        verbose_name=u'Постер',
        upload_to='movies/',
        blank=True,
    )

    year_movie = models.PositiveSmallIntegerField(
        verbose_name=u'Дата выхода',
        default=2019,
    )

    country_movie = models.CharField(
        verbose_name=u'Страна',
        max_length=30,
    )

    directors_movie = models.ManyToManyField(
        Actor,
        verbose_name=u'режиссер',
        related_name="film_director",
    )

    actors_movie = models.ManyToManyField(
        Actor,
        verbose_name=u'актеры',
        related_name="film_actor",
    )

    genres_movie = models.ManyToManyField(
        Genre,
        verbose_name=u'жанры',
    )

    world_premiere_movie = models.DateField(
        verbose_name='Премьера в мире',
        default=date.today,
    )

    budget_movie = models.PositiveIntegerField(
        verbose_name=u'Бюджет',
        default=0,
        help_text=u'указывать сумму в $$$',
    )

    fees_in_usa_movie = models.PositiveIntegerField(
        verbose_name=u'Сборы в США',
        default=0,
        help_text=u'указывать сумму в $$$',
    )

    fess_in_world_movie = models.PositiveIntegerField(
        verbose_name=u'Сборы в мире',
        default=0,
        help_text=u'указывать сумму в $$$',
    )

    category_movie = models.ForeignKey(
        Category,
        verbose_name=u'Категория',
        on_delete=models.SET_NULL,
        null=True,
    )

    url_movie = models.SlugField(
        verbose_name=u'URL',
        max_length=130,
        unique=True,
    )

    draft_movie = models.BooleanField(
        verbose_name=u'Черновик',
        default=False,
    )

    def __str__(self):
        return self.title_movie

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url_movie})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)


class MovieShots(models.Model):
    """Model 'MovieShorts'"""
    class Meta:
        verbose_name = u'Кадр из фильма'
        verbose_name_plural = u'Кадры из фильма'

    title_movie_short = models.CharField(
        verbose_name=u'Заголовок',
        max_length=100,
    )

    description_movie_short = models.TextField(
        verbose_name=u'Описание',
    )

    image_movie_short = models.ImageField(
        verbose_name=u'Изображение',
        upload_to='movie_shots/',
    )

    movie = models.ForeignKey(
        Movie,
        verbose_name=u'Фильм',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title_movie_short


class RatingStar(models.Model):
    """Model 'RatingStar'"""
    class Meta:
        verbose_name = u'Звезда рейтинга'
        verbose_name_plural = u'Звезды рейтинга'
        ordering = ['-value_ratting_star']

    value_ratting_star = models.SmallIntegerField(
        verbose_name=u'Значение',
        default=0,
    )

    def __str__(self):
        return f'{self.value_ratting_star}'


class Rating(models.Model):
    """Model 'Rating'"""
    class Meta:
        verbose_name = u'Рейтинг'
        verbose_name_plural = u'Рейтинги'

    ip_rating = models.CharField(
        verbose_name=u'IP адрес',
        max_length=15,
    )

    star_rating = models.ForeignKey(
        RatingStar,
        on_delete=models.CASCADE,
        verbose_name=u'звезда',
    )

    movie_rating = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name=u'фильм',
        related_name=u'ratings',
    )

    def __str__(self):
        return f'{self.star_rating} - {self.movie_rating}'


class Reviews(models.Model):
    """Model Reviews"""
    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'

    email_review = models.EmailField()
    name_review = models.CharField(
        verbose_name=u'Имя',
        max_length=100,
    )

    text_review = models.TextField(
        verbose_name=u'Сообщение',
        max_length=5000,
    )

    parent_review = models.ForeignKey(
        'self',
        verbose_name=u'Родитель',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    movie_review = models.ForeignKey(
        Movie,
        verbose_name=u'фильм',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name_review} - {self.movie_review}"


class TimeShow(models.Model):
    """Model DateTimeShow"""

    class Meta:
        verbose_name = u'Дата/Время Показа'
        verbose_name_plural = u'Дата/Время показов'

    date_time_show = models.DateTimeField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Дата/Время показа'
    )

    title_film = models.ForeignKey(
        Movie,
        verbose_name=u'Название фильма',
        related_name='film_title_movie',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

    price_ticket = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=u'Стоимость билета'
    )

    def __str__(self):
        return f'{self.date_time_show}'


class HallPlace(models.Model):
    """Hall Place model"""

    class Meta:
        verbose_name = u'Зал'
        verbose_name_plural = u'Залы'

    place = models.CharField(
        unique=True,
        max_length=100,
        blank=True,
        null=True,
        verbose_name=u'Место',
    )

    def __str__(self):
        return f'{self.place}'


class RegistrationVisitors(models.Model):
    """Registration Visitors model"""

    class Meta:
        verbose_name = u'Регистрация Посетителя'
        verbose_name_plural = u'Регистрация Посетителей'

    data_time_show = models.ForeignKey(
        TimeShow,
        verbose_name=u'Дата/Время показа',
        related_name='data_time_show',
        blank=False,
        on_delete=models.PROTECT,
    )

    title_films = models.ForeignKey(
        Movie,
        verbose_name=u'Название',
        related_name='title_film_view_visitor',
        blank=False,
        on_delete=models.PROTECT,
    )

    place_visitor = models.ForeignKey(
        HallPlace,
        verbose_name=u'Место',
        related_name='place_visitor_view',
        blank=False,
        on_delete=models.PROTECT,
    )

    name_visitor = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Посетитель',
    )

    last_name_visitor = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Фамилия',
    )

    email_visitor = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Email',
    )

    price_ticket = models.ForeignKey(
        TimeShow,
        verbose_name=u'Стоимость билета',
        related_name='price_ticket_visitor',
        blank=False,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return (
            f'{self.name_visitor} - '
            f'{self.last_name_visitor}>'
        )
