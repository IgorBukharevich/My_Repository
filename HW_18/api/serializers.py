from mainapp.models import Movie
from mainapp.models import TimeShow
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class TimeShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeShow
        fields = '__all__'
