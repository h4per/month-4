from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from posts.models import Post
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class IndexView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    template_name = "posts/index.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content", "status", "category", "cover"]
    success_url = reverse_lazy("index-bek")


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-bek")


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content", "status", "category", "cover"]
    success_url = reverse_lazy("index-bek")


request = HttpRequest()
def index_bek(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
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


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_update.html", {"post": post})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def post_verify(request):
    context = {
        "title": "Страница верификации",
    }
    return render(request, "posts/post_verify.html", context=context)


# def post_delete(request, pk):
#     if request.method == "POST":
#         post = Post.objects.get(pk=pk)
#         post.delete()
#         return reverse_lazy("index-bek")
#     return render(request, "posts/post_delete.html")


# def post_create(request):
#     if request.method == "POST":
#         post = Post.objects.create(title=request.POST.get("zagolovok"))
#     return render(request, "posts/post_create.html", {"post": post})