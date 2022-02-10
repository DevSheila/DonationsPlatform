

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.LoginPage, name = "login"),
    path('logout/', views.LogoutUser, name = "logout"),
    path('register/', views.RegisterUser, name = "register"),
    path('', views.home, name = "home"),
    
]