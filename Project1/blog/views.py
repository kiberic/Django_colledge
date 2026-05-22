from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

def home(request):
    return render(request, "home.html", {})

def posts(request):
    if request.method == "GET":
        posts = Post.objects.filter(published_at__lte=timezone.now())
        context = {
            "posts": posts
        }
        return render(request, "posts.html", context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "post_detail.html", {"post": post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "add_post.html", {"form" : form})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("posts")
    
# def user_reg(request):
#     if request.method == "POST":
