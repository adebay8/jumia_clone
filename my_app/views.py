from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models 

BASE_JUMIA_URL = 'https://www.jumia.com.ng/catalog/?q={}'
# Create your views here.

def index(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    final_url = BASE_JUMIA_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text

    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('article', {'class': 'prd'})
    
    final_postings = []

    for post in post_listings:
        post_title = post.find('a', {'class',"core"}).find('div', {'class':'info'}).find('h3', {'class':'name'}).text
        post_url = 'https://jumia.com.ng'+ str(post.find('a').get('href'))
        post_price = post.find('a', {'class',"core"}).find('div', {'class':'info'}).find('div', {'class':'prc'}).text
        post_image = post.find('a', {'class',"core"}).find('div', {'class':'img-c'}).find('img').get('data-src')
        
        final_postings.append((post_title, post_url, post_price, post_image))  
    
    user_input = {
        "search": search,
        'final_postings': final_postings,
    }


    return render(request, 'my_app/new_search.html', user_input)