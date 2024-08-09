from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user_model
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Member, Movie
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email




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

def player(request, id):

   member_id = request.session.get('member_id')
   if not member_id:
      # Redirect to sign-in page with 'next' parameter set to the current URL
      signin_url = reverse('signin')  # Get the URL of the sign-in view
      return redirect(f'{signin_url}?next={request.path}')
   
   template = loader.get_template("player.html")
   mymovie = get_object_or_404(Movie, id=id)
   suggested_movies = Movie.objects.exclude(id=mymovie.id).order_by('?')[:5]  # Get 5 random suggested movies
   context = {
      "movie" : mymovie,
      "suggested_movies" : suggested_movies
   }
   return HttpResponse(template.render(context, request))

def movies(request):

   member_id = request.session.get('member_id')
   if not member_id:
      # Redirect to sign-in page with 'next' parameter set to the current URL
      signin_url = reverse('signin')  # Get the URL of the sign-in view
      return redirect(f'{signin_url}?next={request.path}')

   query = request.GET.get('q')
   if query:
      movies_list = Movie.objects.filter(title__icontains=query)
   else:
      movies_list = Movie.objects.all().order_by('-id')

   paginator = Paginator(movies_list, 12)  # Show 12 movies per page
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   template = loader.get_template("movies.html")
   context = {
      'page_obj': page_obj,
      'query': query,  # Pass the query to the template
   }
   return HttpResponse(template.render(context, request))

def signin(request):
   next_url = request.GET.get('next')
   if (request.GET.get('next') != None):
         next_url = request.GET.get('next')
         print(next_url)
   else:
         print("home")
         next_url = 'home'

   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      try:
         member = Member.objects.get(username=username)
         if member.check_password(password):
               # Log the user in
               request.session['member_id'] = member.id
               messages.success(request, 'Login successful!')
               return redirect(next_url)
         else:
               messages.error(request, 'Invalid username or password.')
      except Member.DoesNotExist:
         messages.error(request, 'Invalid username or password.')

   return render(request, 'signin.html', {'next': next_url})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        phone = request.POST.get('phone')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        # Check if username already exists
        if Member.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Invalid email address.')
            return redirect('signup')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        # Create and save the new member
        member = Member(
            username=username,
            email=email,
            password=make_password(password),
            phone=phone,
            firstname=firstname,
            lastname=lastname
        )
        member.save()
        messages.success(request, 'Registration successful. Please sign in.')
        return redirect('signin')

    return render(request, 'signup.html')

def logout(request):
    request.session.pop('member_id', None)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

