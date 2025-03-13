from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class BookListView(generics.ListAPIView):
    """
    View to list all books.

    - Uses `ListAPIView` to provide a read-only list endpoint.
    - Allows unauthenticated users to read but requires authentication for any modification.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.

    - Uses `CreateAPIView` to handle `POST` requests.
    - Only authenticated users can add new books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a specific book by its ID.

    - Uses `RetrieveAPIView` to handle `GET` requests for a single object.
    - Unauthenticated users can view details, but cannot modify.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.

    - Uses `UpdateAPIView` to handle `PUT` and `PATCH` requests.
    - Only authenticated users can modify book details.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.

    - Uses `DestroyAPIView` to handle `DELETE` requests.
    - Only authenticated users can delete a book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# # list all books and create books
# class BookListCreateView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# # Retrieve, update or delete a book by id
# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
