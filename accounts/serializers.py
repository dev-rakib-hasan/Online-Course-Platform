from rest_framework import serializers
from .models import(
    Course,
    Lesson,
    Enrollment,
    LessonProgress,
)

# create your serializer here.
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'slug', 
            'price',
            'thumbnail',
            'course_file',
            'created_at',
            'updated_at',
    ]
        read_only_fields=[
            'id',
            'slug',
            'created_at',
            'updated_at',
        ]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id',
            'course',
            'title',
            'description',
            'slug',
            'video_url',
            'duration',
            'order',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at',
        ]
        
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            'id',
            'course',
            'student',
            'enrolled_at'
            
        ]
        read_only_fields = [
            'id',
            'student',
            'enrolled_at'
        ]

class LesssonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = [
            'id',
            'student',
            'completed',
            'completed_at',    
        ]
        read_only_fields = [
            'id',
            'student',
            'completed_at',
        ]