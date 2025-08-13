from django.db import models

# Create your models here.
# portfolio/models.py
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_awarded = models.DateField()

class SignatureProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
