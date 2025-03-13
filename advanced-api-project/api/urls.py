from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path("api/v1/books/", BookListCreateView.as_view(), name="book-list-create"),
    path("api/v1/books/<int:pk>/", BookDetailView.as_view(), name="book-detail")
]
