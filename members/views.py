from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Member, Movie

# Create your views here.

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def home(request):
    mymovies = Movie.objects.all().order_by('-id')[:3].values()
    template = loader.get_template("home.html")
    context = {
        'movies' : mymovies
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
   mymember = Member.objects.get(id=id)
   template = loader.get_template("detail.html")
   context = {
    'mymember': mymember,
    }
   return HttpResponse(template.render(context, request))

def login(request):
   template = loader.get_template("login.html")
   context = {
      
   }
   return HttpResponse(template.render(context, request))

def register(request):
   template = loader.get_template("register.html")
   context = {
      
   }
   return HttpResponse(template.render(context, request))

def player(request):
   template = loader.get_template("player.html")
   context = {
      
   }
   return HttpResponse(template.render(context, request))

