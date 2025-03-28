from django.urls import path, include
from .views import PostViewSet, CommentViewSet, UserFeedView
from .views import LikePostView, UnlikePostView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", UserFeedView.as_view(), name="user-feed"),
    path("post/<int:pk>/like/", LikePostView.as_view(), name="like-post"),
    path("post/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post")
]
