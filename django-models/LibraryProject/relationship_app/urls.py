from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register
from .views import home_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", register, name="register"),
    path('login/', LoginView.as_view(next_page ="home",template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page ="logout", template_name='relationship_app/logout.html'), name='logout'),
    path("", home_view, name="home"),
]
