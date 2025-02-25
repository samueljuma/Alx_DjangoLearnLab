from .models import Author, Book, Library, Librarian


# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)    
    print(f"Books by {author_name}: {[book.title for book in books]}")



# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books]}")


# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name) 
    librarian = Librarian.objects.get(library=library) 
    print(f"Librarian of {library_name}: {librarian.name}")


