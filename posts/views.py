from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from posts.models import Post, Comment
from django.views import generic
from django.urls import reverse_lazy
from posts.forms import CommentForm, PostForm


class IndexView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    template_name = "posts/index.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    extra_context = {"form": CommentForm()}

    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()
        return redirect("post-detail", pk)


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy("index-bek")


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-bek")


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    form_class = PostForm
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

