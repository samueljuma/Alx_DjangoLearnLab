from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register_view, login_view, logout_view, home_view

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("", home_view, name="home"),
]
