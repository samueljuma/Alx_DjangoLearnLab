from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# list all books and create books
class BookListCreateView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  
# Retrieve, update or delete a book by id
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer