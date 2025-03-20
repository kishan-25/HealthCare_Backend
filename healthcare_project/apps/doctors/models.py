from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    years_of_experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"