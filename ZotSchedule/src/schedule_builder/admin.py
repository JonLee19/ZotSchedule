from django.contrib import admin

from .models import Subject, Course, GraduationPlan, ProjectedEnrollment, Schedule, Enrollment, Student

# Register your models here.
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(GraduationPlan)
admin.site.register(ProjectedEnrollment)
admin.site.register(Schedule)
admin.site.register(Enrollment)
admin.site.register(Student)
