from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category
from .models import Actor
from .models import Genre
from .models import Movie
from .models import MovieShots
from .models import RatingStar
from .models import Rating
from .models import Reviews
from .models import TimeShow
from .models import RegistrationVisitors
from .models import HallPlace
from .models import Hall


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """class viewAdmin Category"""
    list_display = (
        'id',
        'name_category',
        'description_category',
        'url',
    )

    list_display_links = ('name_category',)

    list_filter = ('name_category',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """class viewAdmin Movie"""
    list_display = (
        'id',
        'get_image',
        'title_movie',
        'year_movie',
        'country_movie',
        'category_movie',
        'url_movie',
        'draft_movie',
    )

    list_filter = (
        'category_movie',
        'year_movie',
        'country_movie',
    )

    list_display_links = (
        'title_movie',
    )

    search_fields = (
        'title_movie',
        'category_movie__name_category',
    )

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.poster_movie.url} width="50" height="60"'
        )
    get_image.short_description = 'Постер'


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """class viewAdmin Actor"""
    list_display = (
        'id',
        'name_actor',
        'age_actor',
        'description_actor',
    )

    search_fields = (
        'name_actor',
        'age_actor',
    )

    list_display_links = ('name_actor',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """class viewAdmin Genry"""
    list_display = (
        'id',
        'name_genre',
        'description_genre',
        'url_genre',
    )

    list_display_links = ('name_genre',)

    list_filter = ('name_genre',)

    search_fields = ('name_genre',)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """class viewAdmin MovieShots"""
    list_display = (
        'id',
        'title_movie_short',
        'description_movie_short',
        'movie',
    )

    list_display_links = ('title_movie_short',)

    search_fields = ('title_movie_short',)


@admin.register(RatingStar)
class RatingStar(admin.ModelAdmin):
    """class viewAdmin RatingStar"""
    list_display = (
        'id',
        'value_ratting_star',
    )

    list_display_links = ('value_ratting_star',)

    search_fields = ('value_ratting_star',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """class viewAdmin ReviewsAdmin"""
    list_display = (
        'id',
        'name_review',
        'movie_review',
        'email_review',
        'text_review',
    )

    readonly_fields = (
        'name_review',
        'email_review',
    )

    list_display_links = ('name_review',)

    search_fields = (
        'name_review',
        'movie_review__title_movie',
    )


@admin.register(TimeShow)
class TimeShowAdmin(admin.ModelAdmin):
    """class viewAdmin TimeShow"""
    list_display = (
        'id',
        'date_time_show',
        'title_movie',
        'price_ticket',
        'hall',
    )

    list_display_links = ('date_time_show',)

    search_fields = ('title_movie__title_movie',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """class viewAdmin Rating"""
    list_display = (
        'id',
        'ip_rating',
        'star_rating',
        'movie_rating',
    )

    list_display_links = ('ip_rating',)

    search_fields = (
        'movie_rating__title_movie',
        'ip_rating',
    )


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    """class viewAdmin Hall"""
    list_display = (
        'id',
        'hall_name',
    )

    list_display_links = ('hall_name',)

    search_fields = ('hall_name',)


@admin.register(HallPlace)
class HallPlace(admin.ModelAdmin):
    """class viewAdmin HallPlace"""
    list_display = (
        'id',
        'hall_name',
        'level',
        'place',
    )

    list_display_links = ('place',)

    search_fields = (
        'hall_name__hall_name',
        'place',
        'level',
    )


@admin.register(RegistrationVisitors)
class RegistrationVisitorsAdmin(admin.ModelAdmin):
    """class viewAdmin RegistrationVisitors"""
    list_display = (
        'id',
        'title_movie',
        'name_visitor',
        'last_name_visitor',
        'email_visitor',
    )

    readonly_fields = (
        'name_visitor',
        'last_name_visitor',
        'email_visitor',
    )

    list_display_links = (
        'name_visitor',
        'title_movie',
    )

    search_fields = (
        'name_visitor',
        'last_name_visitor',
        'title_movie__title_movie',
        'email_visitor',
    )
