# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# request = HttpRequest()
def index_bek(requests):
    return HttpResponse ("Главная страница", status=200)

def get_contacts(request):
    return HttpResponse('good', status=500)

def get_about(request):
    return HttpResponse('good 2.0',status=400)

