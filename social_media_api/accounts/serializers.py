from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source="key", read_only=True)  # Get the token key

    class Meta:
        model = Token
        fields = ["token"]

class FollowerSerializer(serializers.ModelSerializer):
    """Serializer for showing followers' basic details"""
    class Meta:
        model = CustomUser
        fields = ["id", "username", "profile_picture"]


class UserSerializer(serializers.ModelSerializer):
    # followers = FollowerSerializer(many=True, read_only=True)
    # following = FollowerSerializer(many=True, read_only=True)
    followers_count = serializers.IntegerField(source="followers.count", read_only=True)
    following_count = serializers.IntegerField(source="following.count", read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "bio", "profile_picture", "followers_count", "following_count"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")
          
        self.context["user"] = user
        return data

    def get_token(self, obj):
        user = self.context.get("user")
        token, _ = Token.objects.get_or_create(user=user)
        return token.key

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
