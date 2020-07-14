from django.db import models

# Create your models here.
class Course(models.Model):
    '''represents an individual class'''
    #description
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=8) #make it 45 for the whole department name?
    number = models.CharField(max_length=10)
    
    #administrative
    code = models.IntegerField('Course Code', default=0)
    type = models.CharField('Lecture, Discussion, Lab, or other', max_length=10)
    section = models.CharField(max_length=2)
    units = models.IntegerField(default=0)
    
    #use
    instructor = models.CharField(max_length=30)
    time = models.CharField(max_length=20)
    place = models.CharField(max_length=15)
    finals = models.CharField(max_length=30) #25?
    
    #more categories to be included
    
    def __str__(self):
        return self.name
    
    def is_online(self):
        return True

class Schedule(models.Model):
    '''represents schedule for one quarter'''
    def __str__(self):
        return 'Generic schedule'

class CoursePlan(models.Model):
    '''represents student's intended 4-year plan'''
    pass


class Student(models.Model):
    pass