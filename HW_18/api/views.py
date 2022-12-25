from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from mainapp.models import Movie
from mainapp.models import TimeShow

from .serializers import MovieSerializer
from .serializers import TimeShowSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TimeShowViewSet(viewsets.ModelViewSet):
    queryset = TimeShow.objects.all()
    serializer_class = TimeShowSerializer

    @action(methods=['get'], detail=False, url_path=r'from_movie/(?P<pk>\d+)')
    def load_list(self, request, pk=None):
        movie_id = get_object_or_404(Movie, id=pk)
        time_show = TimeShow.objects.filter(title_movie=movie_id)
        serializer = TimeShowSerializer(time_show, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
