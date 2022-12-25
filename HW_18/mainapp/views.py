from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from mainapp.models import *
from .forms import RegistrationVisitorsForm


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
    # TODO: ПРОВЕРКА ПРАВИЛЬНОСТИ ПОЛЕЙ ДЛЯ ЗАПОЛЕНИЯ И ТАК ЖЕ ПРИ ПОЛОЖИТЕЛЬНОМ ОТВЕТЕ СОХАРЕНЕНИЯ ЗАПОЛНЕНЫХ ПОЛЕЙ В БД
    :return: registration.html
    """
    error = ''
    if request.method == 'POST':
        form = RegistrationVisitorsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнена неверно!'
    form = RegistrationVisitorsForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'mainapp/registration.html', data)
# -----------------------------------------------------------------------------


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
    list_place = HallPlace.objects.all()
    movie = Movie.objects.filter(id=movie_id).first()
    date_show = TimeShow.objects.filter(title_movie_id=movie)

    context = {
        'movie': movie,
        'date_show': date_show,
        'list_place': list_place,
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
