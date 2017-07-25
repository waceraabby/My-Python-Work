from django.shortcuts import render
from django.http import HttpResponse
# from .models import Students

# Create your views here.

# def welcome(request):
#     return HttpResponse("<p>Welcome to Akirachix</p>")
# def students(request):
#     return HttpResponse("<p>Here we will show all students</p>")
# def teachers(request):
#     return HttpResponse("<p>Here we will show all the teachers</p>")
    
    
    
def welcome(request):
    return render(request, 'welcome_students.html')
def students(request):
    return render(request, '<p>Here we will show all students</p>')