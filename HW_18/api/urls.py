from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet
from .views import TimeShowViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'date_shows', TimeShowViewSet, basename='date_shows')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
