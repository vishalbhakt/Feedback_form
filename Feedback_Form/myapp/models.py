from django.db import models

# Create your models here.

class Feedback_Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=50)
    feedback = models.TextField(max_length=1000)
    rating = models.IntegerField()