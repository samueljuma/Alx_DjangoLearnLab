from django.shortcuts import render
from .models import Author, Book, Librarian
from .models import Library
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in
            return redirect("home")  # Redirect to home after registration
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})


# User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect("home")  # Redirect after login
    else:
        form = AuthenticationForm()

    return render(request, "relationship_app/login.html", {"form": form})


# User Logout view
def logout_view(request):
    logout(request)  # Log the user out
    return redirect("login")  # Redirect to login page


def home_view(request):
    return render(request, "relationship_app/home.html")
