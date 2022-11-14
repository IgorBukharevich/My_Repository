from django.shortcuts import render


def index(request):
    """
    Function Render 'Templates/mainapp/index.html'
    :return: 'index.html'
    """
    return render(request, 'mainapp/index.html')


def base(request):
    """
    Function Render 'Templates/mainapp/base.html'
    :return: base.html
    """
    return render(request, 'mainapp/base.html')


def registration(request):
    """
    Function Render 'Templates/mainapp/registration.html'
    :return: base.html
    """
    return render(request, 'mainapp/registration.html')
