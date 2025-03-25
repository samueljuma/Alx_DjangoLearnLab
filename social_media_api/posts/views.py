from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from .pagination import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination  # Apply pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # Enable filtering
    search_fields = ["title", "content"]  # Allow search by title or content


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination  # Apply pagination
