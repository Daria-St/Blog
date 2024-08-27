from django.shortcuts import render, redirect
from .models import Post, PostCategory

def main(request):
    posts = Post.objects.all()
    category = request.GET.get('category')
    active_category = None
    if category:
        posts = posts.filter(category__id=category)
        active_category = PostCategory.objects.get(id=category)
    categories = PostCategory.objects.all()

    context = {
        "posts": posts,
        'categories': categories,
        'active_category': active_category
    }

    return render(request, 'main.html', context)

    # return render(request, 'main.html', {"posts": posts})


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




