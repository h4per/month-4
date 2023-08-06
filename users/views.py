from django.shortcuts import render
from users.forms import UserRegistrationForm
from django.views import generic
from django.urls import reverse_lazy


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
            return render(request, "registration/register.html", {"user": new_user})
        else:
            user_form = UserRegistrationForm()
            return render(request, "registration/register_done.html", {"form": user_form})