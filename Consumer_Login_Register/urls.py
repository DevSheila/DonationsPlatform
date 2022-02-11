
from django.urls import path, re_path
from . import views

app_name = 'Consumer_Login_Register'

urlpatterns = [
    path('login/', views.ConsumerLoginPage, name = "login"),
    path('logout/', views.ConsumerLogoutUser, name = "logout"),
    path('register/', views.ConsumerRegisterUser, name = "register"),
    path('', views.home, name = "home"),
]