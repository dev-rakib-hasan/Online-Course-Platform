from rest_framework import serializers
from .models import User

# create your serializer here.
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role"]
        
        # def create(self, validated_data):
        #     user = User.object.create_user(**validated_data)
        #     return user
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "role"]