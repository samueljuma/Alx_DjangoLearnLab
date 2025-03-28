from rest_framework.serializers import ModelSerializer
from .models import Post, Comment, Like
from accounts.models import CustomUser

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "profile_picture"]

class PostSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
  
    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "created_at", "updated_at"]
        
    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user  # Set author to logged-in user
        return super().create(validated_data)

class CommentSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ["id", "author", "post", "content", "created_at", "updated_at"]
    
    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user  # Set author to logged-in user
        return super().create(validated_data)


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user", "post", "created_at"]
        read_only_fields = ["id", "user", "created_at"]  # user will be set in the view