from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, home, posts, profile

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html", next_page="profile"), name="login"),
    path("logout/", LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("", home, name="home"),
    path("posts/", posts, name="posts"),
    path("profile/", profile, name="profile"),
]
