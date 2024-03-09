from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. This is the index view of the demoapp")

def home(request):
    return HttpResponse('Welcome to Little Lemon restaurant')