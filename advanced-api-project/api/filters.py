import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet): 
    """
    Custom filter class to enable filtering books by title, author name, and publication year.
    """
    author = django_filters.CharFilter(field_name= "author__name", lookup_expr="icontains") # case insensitive search

    class Meta: 
        model = Book
        fields = ["title", "author", "publication_year"]
