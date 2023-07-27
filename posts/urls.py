from django.urls import path
from posts import views


urlpatterns = [
    path("", views.index_bek, name="index-bek"),
    path('contacts/', views.get_contacts, name='contacts'),   
    path('about/', views.get_about, name='about'),
    path("post/<int:pk>", views.post_detail, name="post-detail"),
    path("post/post_update/<int:pk>", views.post_update, name="post-update"),
    path("post/post_delete/<int:pk>", views.post_delete, name="post-delete"),
]
