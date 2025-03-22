from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="posts" )
  
  def __str__(self):
    return self.title
  
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = models.ImageField(upload_to="profile_pics", default="profile_pics/default.jpg")
  joined_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.user.username}'s profile"

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"{self.author.username}'s comment on {self.post.title}"