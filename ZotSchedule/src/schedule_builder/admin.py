from django.contrib import admin

from .models import Subject, CoursePlan, ProjectedEnrollment, Course, ClassSchedule, Enrollment, Student

# Register your models here.
admin.site.register(Subject)
admin.site.register(CoursePlan)
admin.site.register(ProjectedEnrollment)
admin.site.register(Course)
admin.site.register(ClassSchedule)
admin.site.register(Enrollment)
admin.site.register(Student)
