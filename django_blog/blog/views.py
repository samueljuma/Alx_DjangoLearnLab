from django.shortcuts import render,redirect, get_object_or_404, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from taggit.models import Tag

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


# ------------------------------------------------------------------------------------------------------------------------


# List all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # Template for listing posts
    context_object_name = "posts"
    ordering = ["-published_date"]  # Show latest posts first


# Show details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()  
        return context


# Allow authenticated users to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Use the form
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("post-list")  # Redirect to post list after successful creation


# Allow only the post author to update the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use the form
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to edit
    def get_success_url(self):
            return reverse("post-detail", kwargs={"pk": self.object.pk})

# Allow only the post author to delete the post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow authors to delete

# ------------------------------------------------------------------------------------------------------------

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
      post = get_object_or_404(Post, pk=self.kwargs["pk"])  # Get the related post
      form.instance.post = post
      form.instance.author = self.request.user  # Set comment author
      form.save()
      return redirect("post-detail", pk=post.pk)  # Redirect back to post detail

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.pk})  # Redirect to post detail


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only allow the author to edit

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.pk})  # Redirect to post detail


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only allow the author to delete

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.pk})  # Redirect to post detail

# Search for posts
def search_posts(request):
    query = request.GET.get("q")  # Get search query from URL
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |  # Search in title
            Q(content__icontains=query) |  # Search in content
            Q(tags__name__icontains=query)  # Search in tags
        ).distinct()  # Avoid duplicate results

    return render(request, "blog/search_results.html", {"results": results, "query": query})

def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)  # Get the tag object
    posts = Post.objects.filter(tags=tag)  # Get all posts with this tag

    return render(request, "blog/posts_by_tag.html", {"tag": tag, "posts": posts})
