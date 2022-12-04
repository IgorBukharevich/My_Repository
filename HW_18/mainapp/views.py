from django.shortcuts import render
from mainapp.models import *


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


def registration(request):
    """
    Function Render 'templates/mainapp/registration.html'
    :return: registration.html
    """

    list_movie = Movie.objects.all()
    list_date = TimeShow.objects.all()

    context = {
        'list_movie': list_movie,
        'list_date':  list_date,
    }

    return render(
        request, 'mainapp/registration.html', context
    )


def poster(request):
    """
    Function Render 'templates/mainapp.poster.html'
    :return: poster.html
    """
    poster_img = Movie.objects.all()

    return render(
        request, 'mainapp/poster.html', {'poster_img': poster_img}
        )


def movie_info(request, movie_id: int):
    """
    Function Render 'templates/mainapp.infmovie.html'
    List Movie
    :param movie_id:
    :param request:
    :return:
    """
    movie = Movie.objects.filter(id=movie_id).first()
    context = {
        'movie': movie,
    }

    return render(
        request, 'mainapp/infmovie.html', context
    )


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
