from django.shortcuts import render
from bs4 import Beautifulsoup 
import requests

# Create your views here.

def index(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    
    user_input = {"search": search}
    return render(request, 'my_app/new_search.html', user_input)