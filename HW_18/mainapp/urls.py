from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include


from mainapp.views import *

app_name = 'space_main_apps'

urlpatterns = [
    path('', index, name='home'),
    path('registration', registration, name='registration'),
    path('poster', MovieView.as_view(), name='poster'),
    path(
        '<int:movie_id>/',
        MovieDetailView.as_view(),
        name='movie_info'
    ),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
