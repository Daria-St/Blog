from django.shortcuts import render, redirect
from .models import Post, PostCategory

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {"posts": posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, '', {"posts": posts})

def post_add(request):

    categories = PostCategory.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')

        category_id=request.POST.get('category')
        if title == '' or text == '':
            error = 'Есть незаполненное поле'
            return render(request, 'post_add.html', {'error': error})
        category = PostCategory.objects.get(id=category_id)

        Post.objects.create(title=title, text=text, category=category)
        return redirect('main')

    return render(request, 'post_add.html', {'categories': categories})




