from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def members(request):
    return HttpResponse("Hello world")

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())