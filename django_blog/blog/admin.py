from django.contrib import admin
from .models import Post, Profile, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date", "get_tags"]
    search_fields = ["title", "content"]
    list_filter = ["published_date",] 

    def get_tags(self, obj):
        """Displays tags as a comma-separated list in list_display"""
        return ", ".join(tag.name for tag in obj.tags.all())

    get_tags.short_description = "Tags"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "joined_date", "profile_pic"]
    search_fields = ["user"]
    list_filter = ["joined_date"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created_at"]
    search_fields = ["post", "author"]
    list_filter = ["created_at"]
