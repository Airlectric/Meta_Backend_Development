from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is the index view of the demoapp")

def home(request):
    return HttpResponse('Welcome to Little Lemon restaurant')

def drink(request,drink_name):
    drinks = {
        'mocha' : 'coffee',
        'tea' : 'beverage',
        'coke' : 'soft drink'
    }

    choice_of_drink = drinks.get(drink_name, 'Unknown Drink')
    return HttpResponse(f'<h2>{drink_name}</h2> {choice_of_drink}')