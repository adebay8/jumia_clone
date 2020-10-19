from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

BASE_JUMIA_URL = 'https://www.jumia.com.ng/catalog/?q={}&page={}'
# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account for '+ user + ' was created successfully')
            return redirect('login')

    context = {"form":form}
    return render(request, 'my_app/register.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'my_app/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'base.html')

def new_search(request):
    global search
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    num_pages = 2

    final_postings = []
    i=0

    for pages in range(num_pages):
        pages += 1
        final_url = BASE_JUMIA_URL.format(quote_plus(search), pages)
        response = requests.get(final_url)
        data = response.text

        soup = BeautifulSoup(data, features='html.parser')
        post_listings = soup.find_all('article', {'class': 'prd'})

        for post in post_listings:
            post_id = i
            i+=1
            post_title = post.find('a', {'class',"core"}).find('div', {'class':'info'}).find('h3', {'class':'name'}).text
            post_url = 'https://jumia.com.ng'+ str(post.find('a').get('href'))
            post_price = post.find('a', {'class',"core"}).find('div', {'class':'info'}).find('div', {'class':'prc'}).text
            post_image = post.find('a', {'class',"core"}).find('div', {'class':'img-c'}).find('img').get('data-src')
            
            if post_url == 'https://jumia.com.ngNone':
                continue
            else:
                final_postings.append((post_title, post_url, post_price, post_image, post_id))  
    global user_input

    user_input = {
        "search": search,
        'final_postings': final_postings,
    }

    return render(request, 'my_app/new_search.html', user_input)

def productPage(request, product_id):
    for post in user_input['final_postings']:
        if post[4] == product_id:
            product_details = {
                "search": search,
                'final_postings':[post],
            }
        
    return render(request, 'products/product.html', product_details)