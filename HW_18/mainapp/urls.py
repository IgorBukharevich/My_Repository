from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp.views import *

app_name = 'space_main_apps'

urlpatterns = [
    path('', index, name='home'),
    path('registration', registration, name='registration'),
    path(
        'poster',
        cache_page(60 * 15)
        (MovieView.as_view()),
        name='poster'
    ),
    path(
        '<int:movie_id>/',
        cache_page(60 * 15)
        (MovieDetailView.as_view()),
        name='movie_info'
    ),
    path(
        'about',
        cache_page(60 * 15)
        (about), name='about'),
    path(
        'contact',
        cache_page(60 * 15)
        (contact),
        name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
