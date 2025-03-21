from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")  

        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()

    return render(request, "blog/register.html", {"form": form})


@login_required
def profile_view(request):
    """Display the user profile"""
    return render(request, "blog/profile.html")


@login_required
def update_profile(request):
    """Allow the user to update their profile details"""
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "blog/update_profile.html", context)


def home(request):
    return render(request, "blog/home.html")


def posts(request):
    posts = Post.objects.all()  # Fetch all blog posts
    return render(request, "blog/posts.html", {"posts": posts})
