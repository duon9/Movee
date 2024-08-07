from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
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

def player(request, id):
   template = loader.get_template("player.html")
   mymovie = get_object_or_404(Movie, id=id)
   suggested_movies = Movie.objects.exclude(id=mymovie.id).order_by('?')[:5]  # Get 5 random suggested movies
   context = {
      "movie" : mymovie,
      "suggested_movies" : suggested_movies
   }
   return HttpResponse(template.render(context, request))

def movies(request):
   movies_list = Movie.objects.all()
   template = loader.get_template("movies.html")
   paginator = Paginator(movies_list, 10)

   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context ={'page_obj' : page_obj}
   return HttpResponse(template.render(context, request))

