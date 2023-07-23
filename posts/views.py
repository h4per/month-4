from django.shortcuts import render
from django.http import HttpResponse, HttpRequest 


request = HttpRequest()
def index_bek(request):
    context = {
        "name": "Oleg",
        "title": "Главная страница",
        "my_list": [1,3,4,2]
    }
    return render(request, "posts/index.html", context=context)

 

def get_contacts(request):
    context = {
        "title": "Контакты",
    }
    return render(request, "posts/contacts.html", context)



def get_about(request):
    context = {
        "title": "О нас",
        "content": "Анекдот: колобок моется,моется... Вышел из душа и говорит: 'Блиин я голову забыл помыть'"
    }
    return render(request, "posts/about.html", context)

