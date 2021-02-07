from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def all_characters(request):
    return render(request, 'all_characters.html')

def my_characters(request):
    return render(request, 'my_characters.html')
    
def new_character(request):
    return render(request, 'new_character.html')
    

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
    
def logout(request):
    return render(request, 'new_character.html')