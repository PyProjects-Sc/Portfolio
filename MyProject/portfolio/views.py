from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home(request:HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def about(request:HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

def skills(request:HttpRequest) -> HttpResponse:
    return render(request, 'skills.html')

def projects(request:HttpRequest) -> HttpResponse:
    return render(request, 'projects.html')

def education(request:HttpRequest) -> HttpResponse:
    return render(request, 'education.html')

def certificates(request:HttpRequest) -> HttpResponse:
    return render(request, 'certificates.html')


def contact(request:HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')