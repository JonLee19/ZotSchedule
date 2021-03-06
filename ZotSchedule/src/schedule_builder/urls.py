'''
Created on Jul 11, 2020

@author: Jon Lee
'''

from django.urls import path
from . import views

app_name = 'schedule_builder'

urlpatterns = [
        path('test', views.graduation_plan, name = 'test'),
        
        path('graduation_plan/<int:grad_plan_id>', views.graduation_plan, name = 'graduation_plan'),
        
        path('', views.index, name = 'index'),
        path('contact', views.contact, name = 'contact'),
        path('about', views.about, name = 'about'),
        path('course/<course_name>/', views.course_detail, name = 'course_detail'),
        path('subject/<subject_name>/', views.subject_detail, name = 'subject_detail'),
        path('list_view', views.list_view, name = 'list_view'),
        path('block_view', views.block_view, name = 'block_view'),

        #add more (don't forget the commas)
    ]
