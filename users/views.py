from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RegisterSerializer, ProfileSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from users.utils import get_tokens_for_user
from django.http import request
from .models import User



# Create your views here.
@swagger_auto_schema(method='post',request_body=RegisterSerializer,operation_description="User Registration API")
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registration Successful.", "user": serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', operation_description="Get User Profile API")
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def profile(request):
      serializer = ProfileSerializer(request.user)
      return Response({'message': 'profile retrive successfuly.',
                       'user': serializer.data
})

# login api use jwt
# @swagger_auto_schema(method='post',request_body=LoginSerializer,operation_description="User Login API")
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
    
    
#     email = serializer.validated_data['email']
#     password = serializer.validated_data['password']

#     user = authenticate(request, email=email, password=password)
        

#     if user is not None:
#         tokens = get_tokens_for_user(user)
#         return Response({
#             'message': 'Login successful.',
#             'refresh': str(tokens['refresh']),
#             'access': str(tokens['access']),
#             'user': {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#                 'role': user.role
#             }
#         }, status=status.HTTP_200_OK)
        
#     return Response({'error':'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post',request_body=LoginSerializer,operation_description="User Login API")
@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    email = serializer.validated_data['email']
    password = serializer.validated_data['password']
    
    user = authenticate(request, email=email, password=password)
    
    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response({
            'message': 'Login successful.',
            'refresh': str(tokens['refresh']),
            'access': str(tokens['access']),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        }, status=status.HTTP_200_OK)
        
    return Response({'error':'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)




