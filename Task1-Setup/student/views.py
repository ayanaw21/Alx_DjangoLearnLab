from django.shortcuts import render
from .models import Student,Teacher
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################
def student_list_(request):

    posts = Student.objects.all()

    print(posts) 
    print(posts.query)
    # print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# Part 3
#################################################################
def student_list_(request):
    posts = Student.objects.filter(classroom=1) & Student.objects.filter(age=20)
    print (posts)
    return render(request,'output.html',{'posts':posts})
def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='baldwin') & Q(firstname__startswith ='lakisha'))
    print(posts)
    return render(request,'output.html',{'posts':posts})

# Part 4 || union example
#################################################################
def student_list_(request):
    posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))
    print(posts)
    
    return render(request,"output.html",{'posts':posts})
# Part 5 || union example
#################################################################


###############
# Simple EXCLUDE
###############

def student_list_(request):
    posts = Student.objects.filter(age__gte=20) & Student.objects.filter(firstname__startswith='raquel')
    print(posts)
    return render(request,'output.html',{'posts':posts})
def student_list_(request):
    posts = Student.objects.filter(~Q(age__gt=20) & ~Q(surname__startswith='baldwin'))
    print(posts)
    return render(request,'output.html',{'posts':posts})

# Part 6
#################################################################


###############
# Select and output individual fields
###############

def student_list_(request):
    posts = Student.objects.filter(classroom=3).only("firstname")
    print(posts)
    return render(request,'output.html',{'posts':posts})

    

# Part 6
#################################################################


###############
# Simple performing raw queries
###############

def student_list(request):
    posts = Student.objects.all()
    for s in Student.objects.raw("SELECT * FROM student_student"):
        print (s.classroom)
    print(posts)
    # print(connection.queries)
    return render(request,'output.html',{'data':posts})

