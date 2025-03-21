from django.contrib import admin
from .models import Post, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date"]
    search_fields = ["title", "content"]
    list_filter = ["published_date"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "joined_date", "profile_pic"]
    search_fields = ["user"]
    list_filter = ["joined_date"]
