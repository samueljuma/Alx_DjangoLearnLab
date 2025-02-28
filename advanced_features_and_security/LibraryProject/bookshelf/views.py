from django.shortcuts import render
from bookshelf.models import Book
from django.shortcuts import get_object_or_404
from .forms import ExampleForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required("bookshelf.can_view", raise_exception=True)
def search_books(request):
    search_query = request.GET.get("q", "").strip()
    books = Book.objects.filter(title__icontains=search_query)
    return render(
        request, "bookshelf/book_list.html", {"books": books, "query": search_query}
    )


@permission_required("bookshelf.can_view", raise_exception=True)
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "bookshelf/book_detail.html", {"book": book})


@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/book_form.html", {"form": form})


@permission_required("bookshelf.can_edit", raise_exception=True)
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", book_id=book.id)
    else:
        form = ExampleForm(instance=book)

    return render(request, "bookshelf/book_form.html", {"form": form})


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
