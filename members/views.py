from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.core.paginator import Paginator
from .models import Member, Movie
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout



# Create your views here.
@login_required(redirect_field_name='next', login_url='/signin')
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

@login_required(redirect_field_name='next', login_url='/signin')
def detail(request, id):
   mymember = Member.objects.get(id=id)
   template = loader.get_template("detail.html")
   context = {
    'mymember': mymember,
    }
   return HttpResponse(template.render(context, request))

@login_required(redirect_field_name='next', login_url='/signin')
def player(request, id):
   template = loader.get_template("player.html")
   mymovie = get_object_or_404(Movie, id=id)
   suggested_movies = Movie.objects.exclude(id=mymovie.id).order_by('?')[:5]  # Get 5 random suggested movies
   context = {
      "movie" : mymovie,
      "suggested_movies" : suggested_movies
   }
   return HttpResponse(template.render(context, request))

@login_required(redirect_field_name='next', login_url='/signin')
def movies(request):
   movies_list = Movie.objects.all()
   template = loader.get_template("movies.html")
   paginator = Paginator(movies_list, 10)

   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context ={'page_obj' : page_obj}
   return HttpResponse(template.render(context, request))

def signin(request):

   if (request.GET.get('next') != None):
         next_url = request.GET.get('next')
         print(next_url)
   else:
         print("home")
         next_url = 'home'

   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            # next_url = ""
            # if (request.GET.get('?next') != None):
            #     next_url = request.GET.get('next')
            #     print(next_url)
            # else:
            #     print("home")
            #     next_url = 'home'
            return redirect(next_url)  # Redirect to a home page or any other page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('signin')

   next_url = request.GET.get('next', '')
   return render(request, 'signin.html', {'next': next_url})


def signup(request):
   if request.method == 'POST':
        username = request.POST.get('username')

        if Member.objects.filter(username=username).exists():
           messages.error(request, 'Username already exists')
           return redirect('signup')

        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')


        phone = request.POST.get('phone')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        hashed_password = make_password(password)

        member = Member(username=username, email=email, password=hashed_password, phone = phone, firstname = firstname, lastname = lastname)
        member.save()
        return redirect('home')
   return render(request, "signup.html")

@login_required(redirect_field_name='next', login_url='/signin')
def mlogout(request):
    logout(request)
    return redirect('home')

