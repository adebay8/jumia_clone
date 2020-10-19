from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_JUMIA_URL = 'https://www.jumia.com.ng/catalog/?q={}&page={}'
# Create your views here.

def productPage(request):
    return render(request, 'products/product.html')