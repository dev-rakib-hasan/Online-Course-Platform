from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        INSTRUCTOR = "instructor", "Instructor"
        
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, choices=Role.choices, default=Role.STUDENT)
        