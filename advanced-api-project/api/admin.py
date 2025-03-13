from django.contrib import admin
from .models import Author, Book
from .forms import BookAdminForm

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'get_books')
  
  def get_books(self, obj):
        """Return a comma-separated list of books written by the author."""
        return ", ".join([book.title for book in obj.books.all()])
    
  get_books.short_description = 'Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  form = BookAdminForm
  list_display = ('id','title', 'publication_year', 'author')
