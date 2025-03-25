from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class FollowerSerializer(serializers.ModelSerializer):
    """Serializer for showing followers' basic details"""
    class Meta:
        model = User
        fields = ["id", "username", "profile_picture"]

class UserSerializer(serializers.ModelSerializer):
    followers = FollowerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "followers"]

class RegistrationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
