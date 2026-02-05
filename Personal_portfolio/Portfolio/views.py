
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def certifications(request):
    return render(request, 'certifications.html')

def education(request):
    return render(request, 'education.html')
