'''
Created on Jul 11, 2020

@author: Jon Lee
'''

from django.urls import path
from . import views

app_name = 'schedule_builder'

urlpatterns = [
        path('', views.index, name = 'index'),
        path('<int:course_id>/', views.course_detail, name = 'course_detail'),
        path('<int:subject_id>/', views.subject_detail, name = 'subject_detail'),
        path('list_view', views.list_view, name = 'list_view'),
        path('block_view', views.block_view, name = 'block_view'),
        
        #add more (don't forget the commas)
    ]