from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserProfileView, GetAuthTokenView, FollowUserView, UnfollowUserView


urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("get-token/", GetAuthTokenView.as_view(), name="get_auth_token"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
]
