from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects':projects})

def generator(request):
    return render(request, 'generator/generator.html')