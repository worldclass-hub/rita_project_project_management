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

        # -----------------------------
        # Send to Rita (plain text mail)
        # -----------------------------
        subject = f"New message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        send_mail(subject, body, email, ["ritamarshallubah@gmail.com"])

        # -----------------------------
        # Send confirmation to sender (HTML with WhatsApp emoji button)
        # -----------------------------
        whatsapp_link = "https://wa.me/2347065155030"  # +234 format

        confirm_subject = "Your message has been received"
        confirm_body = f"""
        <p>Hello {name},</p>
        <p>Thank you for reaching out to <b>Rita Marshall</b>. 
        She has received your message and will respond shortly.</p>
        <p>But you can also reach out quickly via WhatsApp:</p>
        <a href="{whatsapp_link}" target="_blank" 
           style="display:inline-flex;align-items:center;background-color:#25D366;
                  color:white;font-weight:bold;padding:10px 15px;border-radius:30px;
                  text-decoration:none;">
            📱 Chat on WhatsApp
        </a>
        <p><br>Best regards,<br>Rita Marshall</p>
        """

        email_message = EmailMessage(
            confirm_subject,
            confirm_body,
            "ritamarshallubah@gmail.com",  # from
            [email],  # to
        )
        email_message.content_subtype = "html"  # mark content as HTML
        email_message.send()

        return JsonResponse({"status": "success", "message": "Message sent successfully!"})

    return JsonResponse({"status": "error", "message": "Invalid request."})
