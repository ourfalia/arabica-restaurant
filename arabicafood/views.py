from django.shortcuts import render
from django.views import generic

# Create your views here.

def get_home(request):
    return render(request, '../templates/home.html')


def go_to_menu(request):
    return render(request, '../templates/menu.html')


def go_to_contact(request):
    return render(request, '../templates/contact.html')
