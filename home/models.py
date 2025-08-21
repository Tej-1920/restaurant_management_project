from django.db import models

# Create your models here.
class Contact(models.Model):
    name=forms.CharField(max_length=50,label="Enter name")
    email=forms.EmailField(label="Enter email")
    message=forms.CharField(widget=forms.Textarea,label="Message")
