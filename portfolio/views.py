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

from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            return JsonResponse({"status": "error", "message": "All fields are required."})

        # Send to Rita
        subject = f"New message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        send_mail(subject, body, email, ["samuelemenike4321@gmail.com"])

        # Send confirmation to sender
        confirm_subject = "Your message has been received"
        confirm_body = f"Hello {name},\n\nThank you for reaching out to Rita Marshall. She has received your message and will respond shortly.\n\nBest regards,\nRita Marshall"
        send_mail(confirm_subject, confirm_body, "samuelemenike4321@gmail.com", [email])

        return JsonResponse({"status": "success", "message": "Message sent successfully!"})

    return JsonResponse({"status": "error", "message": "Invalid request."})
