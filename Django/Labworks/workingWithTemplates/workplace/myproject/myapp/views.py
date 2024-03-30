from django.shortcuts import render
from django.http import HttpResponse

# Create your views here for Home, Menu, About and Booking

def home(request):
    return render(request, 'home.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def about(request):
    return render(request, 'about.html', {})

def book(request):
    return render(request, 'book.html', {})