from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html')

def new_search(request):
    return render(request, 'base.html')