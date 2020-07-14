'''
Created on Jul 11, 2020

@author: Jon Lee
'''

from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name = 'index'),
    ]