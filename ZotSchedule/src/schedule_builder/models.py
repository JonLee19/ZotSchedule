from django.db import models
from django.utils.timezone import now

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
    time = models.CharField(max_length=20) #prob better than a datetime field
    place = models.CharField(max_length=15)
    final = models.CharField(max_length=30) #25?
    
    #more categories to be included
    
    def __str__(self):
        return self.name
    
    def is_online(self):
        if self.place == "VRTL REMOTE":
            return True
        return False

class Schedule(models.Model):
    '''represents schedule for one quarter'''
    def __str__(self):
        return 'Generic schedule'

class CoursePlan(models.Model):
    '''represents student's intended 4-year plan'''
    pass


class Student(models.Model):
    name = models.CharField(max_length=25, default = 'Default Name')
    courses = models.ManyToManyField(Course, related_name='students', through='Enrollment')
    
    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #to save signup times for graphs of when students sign up
    #enroll_date = models.DateTimeField(default=now)
    academic_term = models.CharField(max_length=15)
    
    
    
    