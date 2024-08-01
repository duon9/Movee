from django.urls import path
from . import views

urlpatterns  = [
    path('members/', views.members, name = 'members'),
    path('', views.home, name = "home"),
    path('members/detail/<int:id>', views.detail, name='details'),
    path('login/', views.login, name = "login"),
    path('register/', views.register, name = "register"),
    path('player/<int:id>', views.player, name = "player")
]