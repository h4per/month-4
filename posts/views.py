# from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return HttpResponse ("Главная страница")

def get_contacts(request):
    return HttpResponse('good')

def get_about(request):
    return HttpResponse('good 2.0')

