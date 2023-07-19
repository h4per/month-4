from django.urls import path
from posts import views


urlpatterns = [
    path('contacts/', views.get_contacts, name='contacts'),   
    path('about/', views.get_about, name='about'),
]