from django.urls import path, include
from users import views

urlpatterns = [
    path("users/", include("django.contrib.auth.urls")),
    path("users/register", views.UserRegisterView.as_view(), name="register"),
    path("api/users/list", views.UserListAPIView.as_view(), name="api-users"),
    path("api/users/<int:id>", views.UserDetailAPIView.as_view(), name="api-user"),
]