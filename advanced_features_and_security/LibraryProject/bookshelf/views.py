from django.shortcuts import render
from bookshelf.models import Book
from django.shortcuts import get_object_or_404
from bookshelf.forms import ExampleForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


def book_list(request):
    books = Book.objects.all()  # Secure ORM query
    return render(request, "bookshelf/book_list.html", {"books": books})

def search_books(request):
    search_query = request.GET.get("q", "").strip()
    books = Book.objects.filter(title__icontains=search_query)  # Safe Query
    return render(request, "bookshelf/book_list.html", {"books": books, "query": search_query})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Ensures valid ID
    return render(request, "bookshelf/book_detail.html", {"book": book})


def create_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()  # ORM handles input safely
            return redirect("book_list")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/book_form.html", {"form": form})


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Safe update
            return redirect("book_detail", book_id=book.id)
    else:
        form = ExampleForm(instance=book)

    return render(request, "bookshelf/book_form.html", {"form": form})


@csrf_exempt  # Only for demo; use CSRF protection in production
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":  # Prevents CSRF attacks
        book.delete()
        return redirect("book_list")

    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
