from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        INSTRUCTOR = "instructor", "Instructor"
        
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, choices=Role.choices, default=Role.STUDENT)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()
