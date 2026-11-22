from rest_framework import serializers
from .models import(
    Course,
    Lesson,
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
            'title',
            'description',
            'slug',
            'video_urls',
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