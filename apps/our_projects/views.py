from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def our_projects(request):
    return render(request=request, template_name="our_projects.html")
