from django.urls import path
from .import views

urlpatterns = [
    # Course API URLs
    path('courses/', views.course_list_create, name='course_list_create'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),  
    # Enrollment API URLs
    path('lessons/', views.lesson_list_create, name='lesson_list_create'), 
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    # Enrollment API URLs
    path('enrollments/', views.enrollment_list_create, name='enrollment_list_create'),
    path('enrollment/<int:pk>/', views.enrollment_detail, name='enrollment_detail'),
]
