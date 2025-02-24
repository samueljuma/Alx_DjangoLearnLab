from django.shortcuts import render
from .models import Author, Book, Library, Librarian
# import ListView and DetailView
from django.views.generic import ListView, DetailView


# Function Based Views
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class Based Views
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
