from django.urls import path
from . import views

app_name = 'demoapp'
urlpatterns = [
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('drinks/<str:drink_name>',views.drink, name='drink')
]