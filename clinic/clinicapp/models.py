from django.db import models

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='doctors/')  # Like a photo frame
    created_at = models.DateTimeField(auto_now_add=True)
