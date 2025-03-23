from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import ( 
    register, home, posts, profile_view, update_profile, 
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, CommentCreateView, 
    CommentUpdateView, CommentDeleteView, search_posts, posts_by_tag,
    PostByTagListView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html", next_page="profile"), name="login"),
    path("logout/", LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("", home, name="home"),
    
    #Posts 
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
    path('profile/', profile_view, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    
    # Comments
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    # Search
    path("search/", search_posts, name="post-search"),  # Search URL
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
