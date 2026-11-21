from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import(
    CourseSerializer,
)
from drf_spectacular.utils import(
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)

@extend_schema(
    tags=['Course'],
    summary='List and Create Courses',
    description='Retrieve a list of all courses or create a new course.',
    request=CourseSerializer,
    responses={
        200:CourseSerializer(many=True),
        201:CourseSerializer,
        400:OpenApiResponse(description='Validation Error')
    },
)
    
@api_view(['GET','POST'])
def course_list_create(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    serializer = CourseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@extend_schema(
    tags=['Course'],
    summary='Retrieve, update or delete a course',
    description='Retrieve, update or delete a specific course.',
    request=CourseSerializer,
    responses={
        200:CourseSerializer,
        204:OpenApiResponse(description='Course Deleted Successfully.'),
        400:OpenApiResponse(description='Validation Error'),
        404:OpenApiResponse(description='Course Not Found'),
    },
)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    elif request.method in ['PUT','PATCH']:
        if request.method == 'PATCH':
         serializer = CourseSerializer(course, data=request.data, partial=True)
        else: 
            serializer = CourseSerializer(course, data=request.data)
            
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    