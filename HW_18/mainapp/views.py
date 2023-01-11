from django.shortcuts import render
from django.views.generic.base import View

from mainapp.models import *
from .forms import RegistrationVisitorsForm


class MovieView(View):
    """List Movies"""
    def get(self, request):
        movies = Movie.objects.all().order_by('title_movie')

        context = {
            'movies': movies
        }
        return render(request, 'mainapp/poster.html', context)


class MovieDetailView(View):
    """Full description selected Movie"""
    def get(self, request, movie_id: int):
        """
        Function Render 'templates/mainapp.infmovie.html'
        List Movie
        :param movie_id:
        :param request:
        :return:
        """
        movie = Movie.objects.get(pk=movie_id)

        context = {
            'movie': movie,
        }

        return render(
            request, 'mainapp/infmovie.html', context
        )


def index(request):
    """
    Function Render 'templates/mainapp/index.html'
    :return: 'index.html'
    """
    return render(request, 'mainapp/index.html')


def base(request):
    """
    Function Render 'templates/mainapp/base.html'
    :return: base.html
    """
    return render(request, 'mainapp/base.html')


# -----------------------------------------------------------------------------
def registration(request):
    """
    Function Render 'templates/mainapp/registration.html'
    :return: registration.html
    """
    error = ''
    sucse = ''
    if request.method == 'POST':
        form = RegistrationVisitorsForm(request.POST)
        if form.is_valid():
            form.save()
            sucse = 'Вы успешно забронировали билет!'
        else:
            error = 'Форма заполнена неверно!'
    form = RegistrationVisitorsForm()

    data = {
        'form': form,
        'error': error,
        'sucse': sucse,
    }
    return render(request, 'mainapp/registration.html', data)
# -----------------------------------------------------------------------------


def about(request):
    """
    Function Render 'templates/mainapp.about.html'
    :param request:
    :return:
    """

    return render(
        request, 'mainapp/about.html'
    )


def contact(request):
    """
    Function Render 'templates/mainapp.contact.html'
    :param request:
    :return:
    """
    return render(
        request, 'mainapp/contact.html'
    )
