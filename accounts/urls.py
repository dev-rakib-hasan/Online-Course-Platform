from django.urls import path
from .import views

urlpatterns = [
    # Course API URLs
    path('courses/', views.course_list_create, name='course_list_create'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),    
]
