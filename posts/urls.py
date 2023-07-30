from django.urls import path
from posts import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index-bek"),
    path('contacts/', views.get_contacts, name='contacts'),   
    path('about/', views.get_about, name='about'),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/post_update/<int:pk>", views.PostUpdateView.as_view(), name="post-update"),
    path("post/post_delete/<int:pk>", views.PostDeleteView.as_view(), name="post-delete"),
    path("post/post_create/", views.PostCreateView.as_view(), name="post-create"),
]
