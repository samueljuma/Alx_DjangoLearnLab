from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, home, posts, profile_view, update_profile, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html", next_page="profile"), name="login"),
    path("logout/", LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("", home, name="home"),
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('posts/new/', PostCreateView.as_view(), name='post-create'),  # Create a post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
    path('profile/', profile_view, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
