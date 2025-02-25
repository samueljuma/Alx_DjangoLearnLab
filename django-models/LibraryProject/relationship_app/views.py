from django.shortcuts import render
from .models import Author, Book, Librarian
from .models import Library
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from relationship_app.utils import role_required

@role_required("Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html", {"role": "Admin"})

@role_required("Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html", {"role": "Librarian"})

@role_required("Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html", {"role": "Member"})


# Function Based Views
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class Based Views
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save new user
            login(request, user)  # Log them in
            return redirect("home")  # Redirect to home page
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})


def home_view(request):
    return render(request, "relationship_app/home.html")
