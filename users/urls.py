from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('Login/', views.Login, name='Login')
    path('profile/', views.profile, name='profile'),
]
