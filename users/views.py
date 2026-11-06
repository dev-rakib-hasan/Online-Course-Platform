from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from django.http import request
from .models import User



# Create your views here.
@swagger_auto_schema(method='post',request_body=RegisterSerializer,operation_description="User Registration API")
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registration Successful.", "user": serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
      serializer = ProfileSerializer(request.user)
      return Response({'message': 'profile retrive successfuly.',
                       'user': serializer.data
})

# log in api use jwt



