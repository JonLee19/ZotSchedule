from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course
# Create your views here.

def index(request):
    #shortcut: use render() and get_object_or_404()
    #return HttpResponse("Hello world. You're at the Zotschedule index.")
    #courses = Course.objects.all()
    #template = loader.get_template('schedule_builder/index.html')
    #context = {'courses': courses}
    #return HttpResponse(template.render(context, request))
    courses = Course.objects.order_by('time')
    context = {'courses': courses}
    return render(request, 'schedule_builder/index.html', context)
    

def detail(request, course_id: int):
    '''displays additional course info of selected course'''
    #try: 
    #    course = Course.objects.get(pk=course_id)
    #except Course.DoesNotExist:
    #     raise Http404("Course does not exist")
    #return render(request, 'schedule_builder/detail.html', {'course': course})
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'schedule_builder/detail.html', {'course': course})

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

