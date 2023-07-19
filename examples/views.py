# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


request = HttpRequest()
def test_view(request):
    return HttpResponse("Test")


def test_hello_view(request):
    return HttpResponse('hello', status=500)


def test_bye_view(request):
    return HttpResponse('goodbye')


# def test_view(request):
#     my_list = [1,2,3,4,'oleg']
#     return HttpResponse(my_list)


# def test_view(request):
#     html = "<h1>Этот текст будет полужирным, <i>а этот — ещё и курсивным</i>.</h1>"
#     return HttpResponse(html)


# def test_view(request):
#     html = """<!DOCTYPE html> 
# <html lang="ru"> 
#    <head> 
#       <meta charset="UTF-8"> 
#       <title>Test View</title> 
#    </head> 
#    <body> 
#       <p> 
#          <b> 
#             Этот текст будет полужирным, <i>а этот — ещё и курсивным</i>. 
#          </b> 
#       </p> 
#    </body> 
# </html>"""
#     return HttpResponse(html)


# def test_view(request):
#     my_list = [1,2,3,4,'oleg']
#     headers = {'name': 'oleg'}
#     return HttpResponse(my_list, headers=headers, status=404)


def catch_number_view(request, number):
    return HttpResponse(f"Your num: {number}")


def catch_string_view(request, string):
    return HttpResponse(f"Your string: {string}")
