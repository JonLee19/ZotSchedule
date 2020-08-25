from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Subject, GraduationPlan, ProjectedEnrollment, Course, Schedule, Enrollment, Student

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

def subject_detail(request, subject_name:str):
    '''displays additional info of selected subject'''
    #try: 
    #    course = Course.objects.get(pk=course_id)
    #except Course.DoesNotExist:
    #     raise Http404("Course does not exist")
    #return render(request, 'schedule_builder/detail.html', {'course': course})
    subject = get_object_or_404(Subject, name=subject_name)
    return render(request, 'schedule_builder/subject_detail.html', {'subject': subject})

def graduation_plan(request, grad_plan_id = 1):
    grad_plan = get_object_or_404(GraduationPlan, pk=grad_plan_id)
    grad_plan_by_term = defaultdict(lambda:defaultdict(list)) #nested defaultdicts
    for enrollment in grad_plan.projected_enrollments.all():
        grad_plan_by_term[_convert_to_grade_level(enrollment, grad_plan.start_year)][enrollment.term].append(enrollment.subject)
    context = {'name': grad_plan.name, 'start_year': grad_plan.start_year, 'grad_plan': grad_plan_by_term}
    return render(request, 'schedule_builder/graduationplan.html', context)

def _convert_to_grade_level(enrollment: ProjectedEnrollment, start_year:int):
    '''converts enrollment year and term info to year level in school, starting at year1'''
    grade_level = (enrollment.year - start_year)+ (1 if enrollment.term=='Fall' else 0)
    return f'year{grade_level}'
    
    #if (enrollment.year == start_year and enrollment.term == "Fall") or (enrollment.year == start_year+1 and enrollment.term !="Fall"):
    #    return "year1"
    #elif (enrollment.yearA == start_year+1 and enrollment.term == "Fall") or (enrollment.year == start_year+2 and enrollment.term !="Fall"):
    #    return "year2"
    #elif (enrollment.year == start_year+2 and enrollment.term == "Fall") or (enrollment.year == start_year+3 and enrollment.term !="Fall"):
    #    return "year3"
    #elif (enrollment.year == start_year+2 and enrollment.term == "Fall") or (enrollment.year == start_year+3 and enrollment.term !="Fall"):
    #    return "year4"
    #else:
    #    return "unknown"
    

        

def test(request, grad_plan_id=1):
    grad_plan = get_object_or_404(GraduationPlan, pk=grad_plan_id)
    for course in grad_plan.subjects.all():
        return HttpResponse("the year is "+course.year())

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

def about(request):
    return render(request, 'schedule_builder/about.html', {})

def contact(request):
    return render(request, 'schedule_builder/contact.html', {})
