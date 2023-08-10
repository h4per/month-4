from django.shortcuts import render
from users.forms import UserRegistrationForm
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail

from users.serializers import UserSerializer, UserDetailSerializer
from rest_framework import generics
from users.models import GeekUser
from users.forms import UserRegistrationForm


class UserListAPIView(generics.ListAPIView):
    queryset = GeekUser.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = GeekUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "id"


class UserRegisterView(generic.CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.clean_password2())
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
        return render(request, "registration/register.html", {"form": user_form})


def email_view(request):
    subject = 'Сброс пароля'
    message = 'registration/password_reset_email.html'
    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from)
    return render("registration/password_reset_confirm.html")