from django.urls import path
from .views import (
    book_list,
    search_books,
    book_detail,
    create_book,
    update_book,
    delete_book,
)

urlpatterns = [
    path("", book_list, name="book_list"),
    path("search/", search_books, name="search_books"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
    path("book/add/", create_book, name="create_book"),
    path("book/<int:book_id>/edit/", update_book, name="update_book"),
    path("book/<int:book_id>/delete/", delete_book, name="delete_book"),
]
