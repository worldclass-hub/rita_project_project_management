from django.shortcuts import render

# portfolio/views.py
from .models import Certificate, SignatureProject

def welcome_view(request):
    return render(request, 'portfolio/welcome.html')  # You'll need to create this template


def all_certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/all_certificates.html', {'certificates': certificates})

def all_signature_projects(request):
    projects = SignatureProject.objects.all()
    return render(request, 'portfolio/all_signature_projects.html', {'projects': projects})
