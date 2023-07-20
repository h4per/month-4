# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# request = HttpRequest()
def index_bek(requests):
    return HttpResponse ("Главная страница", status=200)


def get_contacts(request):
    return HttpResponse('Контакты', status=200)


def get_about(request):
    return HttpResponse('О нас',status=200)

