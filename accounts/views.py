from django.shortcuts import render
from . import models

# Create your views here.

def accountsPage(request):
    return render(request, 'accounts/accountsPage.html')