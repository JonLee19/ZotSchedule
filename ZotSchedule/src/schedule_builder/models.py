from django.db import models
#from django.utils.timezone import now

#globals
current_term = "Fall 2020"

#REMEMBER TO THINK ABOUT WHETHER on_delete NEEDS TO BE CASCADE, or SET NULL
#https://simpleisbetterthancomplex.com/tips/2016/07/25/django-tip-8-blank-or-null.html

#Graduation Plans

class Subject(models.Model):
    '''represents a generic class offered for instruction, distinct from any individual offering of that class'''
    #description
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=8) #make it 45 for the whole department name?
    number = models.CharField(max_length=10)
    co_reqs = None #set as a many to one rel to self, on delete = set null, blank= true
    pre_reqs = None
    satisfies = None #req's like GE's it satisfies
    terms_offered = None #fall/winter/spring
    
    def num_students_taking(self):
        return NotImplemented
    
    def add_to_student(self):
        return NotImplemented
    
    def most_recent(self):
        return NotImplemented
    
    def is_uppderdiv(self):
        if self.number >= 100:
            return True
        return False
    
    def __str__(self):
        return self.name
    
    
class GraduationPlan(models.Model):
    '''represents student's intended 4-year plan'''
    name = models.CharField(max_length=25, default = 'Default Name') #owner
    subjects = models.ManyToManyField(Subject, related_name='graduation_plans', through='ProjectedEnrollment')
    
    start_year = None
    
    def add_to_student_record(self):
        return NotImplemented
        
    def __str__(self):
        return self.name
    
class ProjectedEnrollment(models.Model):
    '''represents a student's intent to take a class of a subject during a given academic term'''
    #b/c its through this 3rd party class, deletions of one obj will only get rid of the 3rd party join table, not the other obj

    subject = models.ForeignKey(Subject, related_name='projected_enrollments', on_delete=models.CASCADE, default = 1)#test subject is id = 10
    graduation_plan = models.ForeignKey(GraduationPlan, related_name='projected_enrollments', on_delete=models.CASCADE, default = 1) #test
    academic_term = models.CharField(max_length=15, default = current_term)
    
    #enroll_date = models.DateTimeField(default=now) 
    #to save signup times for graphs of when students usually sign up for the class
    
    def __str__(self):
        #return "default name"
        return self.subject.name + ": " + self.graduation_plan.name





#Class Scheduling


#for planning current quarter's classes
class Course(models.Model): #only used on scheduling view/db
    '''represents an individual offering of a class'''
    
    subject = models.ForeignKey(Subject, related_name="history", on_delete=models.CASCADE)#, default = 1
    
    name = models.CharField(max_length=30, default = "default course")
    
    #administrative
    code = models.IntegerField('Course Code', default=00000)
    type = models.CharField('Lecture/Dis/Lab/Sem', max_length=10)
    section = models.CharField(max_length=4)
    units = models.IntegerField(default=0)
    
    #practical use
    instructor = models.CharField(max_length=30, default = 'TBA')
    time = models.CharField(max_length=20, default = 'TBA') #prob better than a datetime field
    place = models.CharField(max_length=15, default = 'TBA')
    final = models.CharField(max_length=30, default = 'TBA') #25?
    
    #more categories to be included:
    #-enrollment_restrictions #major locked?
    #-when ppl can enroll, if they have to be upperclassmen, when restrictions drop
    
    @classmethod
    def create(cls, subject: Subject, **kwargs):
        '''alternate constructor'''
        course = cls(subject = subject)
        fields = (attr for attr in subject.__dict__ if not attr.startswith('_') and attr!="id")
        subj_attr = {attr: subject.__dict__[attr] for attr in fields}
        course.__dict__.update(subj_attr)
        course.__dict__.update(kwargs)
        return course
    
    def is_online(self):
        if self.place == "VRTL REMOTE":
            return True
        return False
    
    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    '''represents a schedule of classes for the current academic term'''
    
    name = models.CharField(max_length=25, default = 'Default Name') #owner
    #academic_term = models.CharField(max_length=15, default = current_term)
    courses = models.ManyToManyField(Course, related_name='students', through='Enrollment')
    
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    '''represents a student's enrollment in a course'''
    
    
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, related_name='enrollments', on_delete=models.CASCADE)
    academic_term = models.CharField(max_length=15, default = current_term)
    #
    ##to save signup times for graphs of when students sign up
    ##enroll_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.course.name + ": " + self.schedule.name




#return to this later, build user profile with use
class Student(models.Model):
    '''represents a student user, including all subjects planned'''
    #will hold references to both the student's current schedule and graduation plan
    
    
    #db only needs to hold the students transcript, not actually what current courses they are on
    name = models.CharField(max_length=25, default = 'Default Name')
    grade = None
    #transcript = None
    #course_plan = models.OneToOneField(GraduationPlan, on_delete=models.CASCADE, default = None)
    #schedule = models.OneToOneField(ClassSchedule, on_delete=models.CASCADE, default = None)
    
    
    
    def gpa(self):
        return NotImplemented
    
    def get_transcript(self):
        return NotImplemented
    
    def __str__(self):
        return self.name
    
    


    

    
    
    
    
    
def check_state():
#from schedule_builder.models import Course, Subject, Schedule, Student, Enrollment, GraduationPlan, ProjectedEnrollment, check_state
    l = []
    l.append("Courses: "+", ".join([str(c) for c in Course.objects.all()]))
    l.append("Subjects: "+", ".join([str(s) for s in Subject.objects.all()]))
    l.append("Students: "+", ".join([str(s) for s in Student.objects.all()]))
    l.append("Course Plan: "+", ".join([str(c) for g in GraduationPlan.objects.all()]))
    l.append(f"Enrollments: {{{'; '.join([str(e) for e in Enrollment.objects.all()])}}}")
    l.append(f"Projected Enrollments: {{{'; '.join([str(e) for e in ProjectedEnrollment.objects.all()])}}}")
    print('\n'.join(l))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#return to:

# Create your models here.

current_curriculum = {}
all_subjects = {}
current_subjects = {}
past_subjects = {}

past_classes = {}