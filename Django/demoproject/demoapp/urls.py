from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('drinks/<str:drink_name>',views.drink, name='drink')
]