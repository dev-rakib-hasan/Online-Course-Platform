from rest_framework import serializers
from .models import(
    Course,
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