from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserProfileView, GetAuthTokenView


urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("get-token/", GetAuthTokenView.as_view(), name="get_auth_token"),
]
