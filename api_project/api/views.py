from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

class BookList(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]
