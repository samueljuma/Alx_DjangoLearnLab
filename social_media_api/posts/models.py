from django.db import models
from accounts.models import CustomUser


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # delete posts if user is deleted
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # delete comments if post is deleted
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # delete comments if user is deleted
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Like(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE) # delete likes if post is deleted
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # delete likes if user is deleted
