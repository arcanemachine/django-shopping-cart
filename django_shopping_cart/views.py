# from django.http import HttpResponse
from django.shortcuts import render

def project_root(request):
    return render(request, 'project_root.html')
