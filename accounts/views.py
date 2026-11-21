from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import(
    SignupSerializer,
    SigninSerializer,
    ProfileSerializer
)

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse, 
    OpenApiTypes,
)

@extend_schema(
    tags=['Signup'],
    summary='User Signup',
    description='This endpoint allows users to sign up by providing their username and password.',
    request=SignupSerializer,
    responses={
        201:OpenApiResponse(description='Signup successfully.'),
        400:OpenApiResponse(description='Bad request.'),
    },
)

@api_view(['POST'])
def Signup(request):
    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {
                'message': 'Signup Successful.',
                'user': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@extend_schema(
    tags=['Signin'],
    summary='User Signin',
    description='This endpoint allows users to sign in by providing their username and password.',
    request=SigninSerializer,
    responses={
        200: OpenApiResponse(description='Signin successfully.'),
        400: OpenApiResponse(description='Bad request.'),
        401: OpenApiResponse(description='Invalid credentials.'),
    },
)

@api_view(['POST'])
def Signin(request):
    serializer = SigninSerializer(data=request.data)

    if serializer.is_valid():
        # এখানে email/password check হবে
        # এবং JWT token generate হবে

        return Response(
            {
                'message': 'Signin Successful.',
                'user': serializer.data
            },
            status=status.HTTP_200_OK
        )

    return Response(
        serializer.errors,
        status=status.HTTP_401_UNAUTHORIZED
    )

@extend_schema(
    tags=['Profile'],
    summary='User Profile',
    description='This endpoint allows authenticated users to view their profile information.',
    responses={
        200: OpenApiResponse(description='Profile retrieved successfully.'),
        401: OpenApiResponse(description='Unauthorized.'),
    },
)
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def Profile(request):
    serializer = ProfileSerializer(request.user)

    return Response(
        {
            'message': 'Profile Retrieved Successfully',
            'user': serializer.data
        },
        status=status.HTTP_200_OK
    )