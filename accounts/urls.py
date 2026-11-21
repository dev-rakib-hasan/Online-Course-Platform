from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.Signup, name='signup'),
    path('signin/', views.Signin, name='signin'),
    path('profile/', views.Profile,name='profile'),
]
