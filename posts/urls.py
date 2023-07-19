from django.urls import path
from posts import views


urlpatterns = [
    path("", views.index_bek, name="index-bek"),
    path('contacts/', views.get_contacts, name='contacts'),   
    path('about/', views.get_about, name='about'),
]