from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course, Subject, CoursePlan, ClassSchedule, Enrollment, Student, ProjectedEnrollment

from collections import defaultdict
# Create your views here.

department_abbrevs = {}


#set/get cookies
#def setcookie(request):  
#    response = HttpResponse("Cookie Set")  
#    response.set_cookie('java-tutorial', 'javatpoint.com')  
#    return response  
#def getcookie(request):  
#    tutorial  = request.COOKIES['java-tutorial']  
#    return HttpResponse("java tutorials @: "+  tutorial);  
#add to url patterns:
#path('scookie',views.setcookie),  
#path('gcookie',views.getcookie)  
#also see sessions/get sessions

def index(request):
    #shortcut: use render() and get_object_or_404()
    #return HttpResponse("Hello world. You're at the Zotschedule index.")
    #courses = Course.objects.all()
    #template = loader.get_template('schedule_builder/index.html')
    #context = {'courses': courses}
    #return HttpResponse(template.render(context, request))
    courses = Course.objects.order_by('time')
    subjects = Subject.objects.all()
    context = {'courses': courses, 'subjects': subjects}
    
    return render(request, 'schedule_builder/index.html', context)
    

def course_detail(request, course_name: str):
    '''displays additional info of selected course'''
    #try: 
    #    course = Course.objects.get(pk=course_id)
    #except Course.DoesNotExist:
    #     raise Http404("Course does not exist")
    #return render(request, 'schedule_builder/detail.html', {'course': course})
    course = get_object_or_404(Course, name=course_name)
    return render(request, 'schedule_builder/course_detail.html', {'course': course})

def subject_detail(request, subject_id: int):
    '''displays additional info of selected subject'''
    #try: 
    #    course = Course.objects.get(pk=course_id)
    #except Course.DoesNotExist:
    #     raise Http404("Course does not exist")
    #return render(request, 'schedule_builder/detail.html', {'course': course})
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'schedule_builder/subject_detail.html', {'subject': subject})

def course_plan(request, course_plan_id: int):
    course_plan = get_object_or_404(pk=course_plan_id)
    courses_by_year = defaultdict(list)
    for course in course_plan.courses:
        courses_by_year[course.academic_term].append(course)
    context = {'name': course_plan.name, 'course_plan': courses_by_year}
    return render(request, 'schedule_builder/courseplan.html', context)



def list_view(request):
    pass

def block_view(request):
    pass

def edit_view(request):
    pass

def search_classes():
    pass

def see_prerequisites():
    pass

def course_restrictions():
    pass

def schedule_view():
    pass

