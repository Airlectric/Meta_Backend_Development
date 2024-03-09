from django.shortcuts import render
from django.http import HttpResponse

def drinks(request, drink_name):
    drink = {
    'mocha' : 'coffee',
    'tea' : 'beverage',
    'lemonade' : 'refreshment'
    }

    choice_of_drink = drink.get(drink_name, 'Unknown drink')
    return HttpResponse(f'<h2> {drink_name}</h2> {choice_of_drink}')
