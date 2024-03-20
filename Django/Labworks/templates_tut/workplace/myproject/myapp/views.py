from django.shortcuts import render

# Create your views here for menu.

# Create view for About
def menu(request):
    return render(request,'menu.html',{'menu':'choose your choice'})

# Create view for Menu
def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request,'about.html',about_content)