from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp.views import *

app_name = 'space_main_apps'

urlpatterns = [
    path('', index, name='home'),
    path('registration', registration, name='registration'),
    path('poster', poster, name='poster'),
    path('movie_info/<int:movie_id>', movie_info, name='movie_info'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    # path('get_movie', get_movie, name='get_movie'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
