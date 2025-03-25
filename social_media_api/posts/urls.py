from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("post/comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
