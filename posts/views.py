from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from posts.models import Post


request = HttpRequest()
def index_bek(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


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


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_update.html", {"post": post})


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_delete.html", {"post": post})
