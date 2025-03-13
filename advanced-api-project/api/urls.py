from django.urls import path
from .views import BookCreateView, BookDetailView, BookListView, BookDeleteView, BookUpdateView

urlpatterns = [
    path("api/v1/books/", BookListView.as_view(), name="book-list"),
    path("api/v1/books/add/", BookCreateView.as_view(), name="book-add"),
    path("api/v1/books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("api/v1/books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
    path("api/v1/books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]
