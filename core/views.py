from django.shortcuts import render, redirect
from .models import Post, PostCategory, PostComment
from .forms import PostAddForm

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

def post_detail(request, post_id):
    post= Post.objects.get(id=post_id)
    comments = PostComment.objects.filter(post=post)
    return render(request, 'post_detail.html', {"post": post, 'comments': comments})


def post_add(request):

    categories = PostCategory.objects.all()
    post_add_form = PostAddForm()

    if request.method == "POST":
        post_add_form = PostAddForm(request.POST)
        if post_add_form.is_valid():
            data = post_add_form.cleaned_data
            Post.objects.create(title=data['title'],
                                text=data['text'],
                                category=data['category'])
            return redirect('main')

    context = {
        'categories':categories,
        'post_add_form':post_add_form
    }
    return render(request, 'post_add.html', context)



# def post_add(request):
#
#     categories = PostCategory.objects.all()
#
#     if request.method == "POST":
#         title = request.POST.get('title')
#         text = request.POST.get('text')
#
#         category_id=request.POST.get('category')
#         if title == '' or text == '':
#             error = 'Есть незаполненное поле'
#             return render(request, 'post_add.html', {'error': error})
#         category = PostCategory.objects.get(id=category_id)
#
#         Post.objects.create(title=title, text=text, category=category)
#         return redirect('main')
#
#     return render(request, 'post_add.html', {'categories': categories})


def comment_add(request, post_id):
    if request.method == 'POST':
        post= Post.objects.get(id=post_id)
        text = request.POST.get('text')
        PostComment.objects.create(post=post, text=text)

        return redirect('post_detail', post.id)


