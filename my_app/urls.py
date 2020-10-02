from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [     
    path('', views.index, name='home'),
    path('searchResult/', views.new_search, name='new_search'), 
]