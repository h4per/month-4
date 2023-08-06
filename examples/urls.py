from django.urls import path
from examples import views


urlpatterns = [
    path('test/', views.test_view, name='test-view'),
    path('test/hello', views.test_hello_view, name='test-hello'),
    path('test/goodbye', views.test_bye_view, name='test-bye'),
    path('test/<int:number>', views.catch_number_view, name='catch-number'),
    path('test/<str:string>/test', views.catch_string_view, name='catch-string'),
    path('test/email', views.email_view, name='email-view'),
]