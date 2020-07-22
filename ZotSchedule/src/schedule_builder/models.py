from django.db import models
#from django.utils.timezone import now

# Create your models here.
current_term = "Fall 2020"
current_curriculum = {}
all_subjects = {}
current_subjects = {}
past_subjects = {}

past_classes = {}



#for 4-year course plan
class Subject(models.Model):
    '''represents a general class offered for instruction, distinct from any individual offering of that class'''
    #description
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=8) #make it 45 for the whole department name?
    number = models.CharField(max_length=10)
    co_reqs = None
    pre_reqs = None
    satisfies = None #req's like GE's it satisfies
    terms_offered = None #fall/winter/spring
    
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
    
    
class CoursePlan(models.Model):
    '''represents student's intended 4-year plan'''
    name = models.CharField(max_length=25, default = 'Default Name') #owner
    courses = models.ManyToManyField(Subject, related_name='course_plans', through='ProjectedEnrollment')
    
    start_year = None
    
    def add_to_student_record(self):
        return NotImplemented
        
    def __str__(self):
        return self.name
    
class ProjectedEnrollment(models.Model):
    '''represents a student's intent to take a class of a subject during a given academic term'''
    subject = models.ForeignKey(Subject, related_name='projected_enrollments', on_delete=models.CASCADE)
    course_plan = models.ForeignKey(CoursePlan, related_name='projected_enrollments', on_delete=models.CASCADE)
    academic_term = models.CharField(max_length=15, default = current_term)
    
    #enroll_date = models.DateTimeField(default=now) #to save signup times for graphs of when students sign up
    
    def __str__(self):
        return self.subject.name + ": " + self.course_plan.name








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
    
class ClassSchedule(models.Model):
    '''represents schedule for one quarter'''
    
    def __str__(self):
        return 'Generic schedule'

class Student(models.Model):
    '''represents a student user, including all subjects planned'''
    #db only needs to hold the students transcript, not actually what current courses they are on
    name = models.CharField(max_length=25, default = 'Default Name')
    grade = None
    #transcript = None
    #course_plan = models.OneToOneField(CoursePlan, on_delete=models.CASCADE, default = None)
    #schedule = models.OneToOneField(ClassSchedule, on_delete=models.CASCADE, default = None)
    
    courses = models.ManyToManyField(Subject, related_name='students', through='Enrollment')
    
    def gpa(self):
        return NotImplemented
    
    def get_transcript(self):
        return NotImplemented
    
    def __str__(self):
        return self.name
    
    
class Enrollment(models.Model):
    '''represents a student's enrollment in a course'''
    course = models.ForeignKey(Subject, related_name='enrollments', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.CASCADE)
    academic_term = models.CharField(max_length=15, default = current_term)
    #to save signup times for graphs of when students sign up
    #enroll_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.course.name + ": " + self.student.name


    

    
    
    
    
    
def check_state():
#from schedule_builder.models import Course, Subject, Student, Enrollment, CoursePlan, ProjectedEnrollment, check_state
    l = []
    l.append("Courses: "+", ".join([str(c) for c in Course.objects.all()]))
    l.append("Subjects: "+", ".join([str(s) for s in Subject.objects.all()]))
    l.append("Students: "+", ".join([str(s) for s in Student.objects.all()]))
    l.append("Course Plan: "+", ".join([str(c) for c in CoursePlan.objects.all()]))
    l.append(f"Enrollments: {{{'; '.join([str(e) for e in Enrollment.objects.all()])}}}")
    l.append(f"Projected Enrollments: {{{'; '.join([str(e) for e in ProjectedEnrollment.objects.all()])}}}")
    print('\n'.join(l))