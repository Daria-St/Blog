from django.shortcuts import render
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {"posts": posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, '', {"posts": posts})
