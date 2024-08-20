from django.shortcuts import render, redirect
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {"posts": posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, '', {"posts": posts})

def post_add(request):

    return render(request, 'post_add.html')

def post_add_submit(request):
    title = request.POST.get('title')
    text = request.POST.get('text')

    Post.objects.create(title=title, text=text)

    print(title, text)
    return redirect('main')