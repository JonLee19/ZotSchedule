'''
Created on Jul 11, 2020

@author: Jon Lee
'''

from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name = 'index'),
        path('', views.list_view, name = 'list view'),
        path('', views.block_view, name = 'block view'),
        
        #add more (don't forget the commas)
    ]