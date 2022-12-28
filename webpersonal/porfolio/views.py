from django.shortcuts import render
from .models import Project

def porfolio(request):
    project = Project.objects.all()
    return render (request, "porfolio/porfolio.html",{'projects': project})