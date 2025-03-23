from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from taggit.forms import TagField, TagWidget


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ["bio", "profile_pic"]

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(), required=False) # Adding tags field with TagWidget
    
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"] 
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Write your comment..."}
            ),
        }
