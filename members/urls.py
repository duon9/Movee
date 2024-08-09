from django.urls import path
from . import views

urlpatterns  = [
    path('members/', views.members, name = 'members'),
    path('', views.home, name = "home"),
    path('members/detail/<int:id>', views.detail, name='details'),
    path('player/<int:id>', views.player, name = "player"),
    path('movies/', views.movies, name = 'movies'),
    path('signin/', views.signin, name = "signin"),
    path('signup/', views.signup, name = "signup"),
    path('logout', views.mlogout, name = "logout")
]