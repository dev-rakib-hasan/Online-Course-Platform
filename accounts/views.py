from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import(
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)
from .models import(
    Course,
    Lesson,
    Enrollment,
    LessonProgress,
)

from .serializers import(
    CourseSerializer,
    LessonSerializer,
    EnrollmentSerializer,
    LesssonProgressSerializer
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
#===============
# Course API
#=============== 
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
 
#================
# Lesson API
#================

@extend_schema(
    tags=['Lesson'],
    summary='List and Create Lesson',
    description='Retrieve a list of all lesson or create a new lesson.',
    request=LessonSerializer,
    responses={
        200:LessonSerializer(many=True),
        204:LessonSerializer,
        400:OpenApiResponse(description='Validation Error')
    },
)
    
# Lesson List & Create
@api_view(['GET','POST'])
def lesson_list_create(request):
    if request.method == 'GET':
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    serializer = LessonSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@extend_schema(
    tags=['Lesson'],
    summary='Retrieve, Update or Delete Lesson.',
    description='Retrieve Update or Delete Specific Lesson.',
    request=LessonSerializer,
    responses={
        200:LessonSerializer,
        204:OpenApiResponse(description='Lesson Deleted Successfully.'),
        400:OpenApiResponse(description='Validation Error.'),
        404:OpenApiResponse(description='Lesson Not Found')
    },
)

# Lesson Detail, Update & Delete
@api_view(['GET','PUT','PATCH','DELETE'])
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'GET':
      serializer = LessonSerializer(lesson)
      return Response(serializer.data)
  
    elif request.method in ['PUT','PATCH']:
        if request.method == 'PATCH':
           serializer = LessonSerializer(lesson, data=request.data, partial=True)
        else:
          serializer = LessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
     
    elif request.method == 'DELETE':
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#==================
# Enrollment API
#==================

@extend_schema(
    tags=['Enrollment'],
    summary='Get all enrollments',
    description='Get all enrollments of the logged-in student.',
    request=EnrollmentSerializer,
    responses={
        200: EnrollmentSerializer(many=True)
    }
)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def enrollment_list_create(request):
    if request.method == 'GET':
        enrollment = Enrollment.objects.filter(
            student = request.user
        )
        serializer = EnrollmentSerializer(enrollment, many=True)
        return Response(serializer.data)
    serializer = EnrollmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(student=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@extend_schema(
    tags=['Enrollment'],
    summary='Get enrollment details',
    description='Retrieve a specific enrollment by ID.',
    request=EnrollmentSerializer,
    responses={
        200: EnrollmentSerializer,
        404: OpenApiResponse(description='Enrollment not found')
    }
)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def enrollment_detail(request, pk):
    try:
       enrollment = Enrollment.objects.get(pk=pk, student=request.user)
    except Enrollment.DoesNotExist:
        return Response({'message':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EnrollmentSerializer(enrollment)
    return Response(serializer.data)

#========================
# Lesson Progress API
#========================

@api_view(['POST'])
def lesson_progress(request):
    serializer = LesssonProgressSerializer(data=request.data)
      
    if serializer.is_valid():
          serializer.save(student=request.user) 
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.erro,status=status.HTTP_404_NOT_FOUND)
  
