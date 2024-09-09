from django.shortcuts import render, redirect
from .models import Post, PostCategory, PostComment, Feedback
from .forms import PostAddForm, CommentAddForm, FeedbackAddForm, PostAddModelForm

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
    comment_add_form = CommentAddForm()
    post= Post.objects.get(id=post_id)
    comments = PostComment.objects.filter(post=post)
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        comment_add_form = CommentAddForm(request.POST)
        if comment_add_form.is_valid():
            data = comment_add_form.cleaned_data
        PostComment.objects.create(post=post, text=data['text'])
        return redirect('post_detail', post.id)

    context = {
        "post": post,
        'comments': comments,
        'comment_add_form': comment_add_form
    }
    return render(request, 'post_detail.html', context)


def post_add(request):

    categories = PostCategory.objects.all()
    post_add_form = PostAddModelForm()

    if request.method == "POST":
        post_add_form = PostAddModelForm(request.POST)
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

def feedback_add(request):
    feedback_add_form = FeedbackAddForm()
    if request.method == "POST":
        feedback_add_form = FeedbackAddForm(request.POST)

        if feedback_add_form.is_valid():
            data = feedback_add_form.cleaned_data
            print(data)
            Feedback.objects.create(name=data['name'], text=data['text'])
            return redirect('feedback_done')

    context = {
        'feedback_add_form' : feedback_add_form
    }

    return render(request, 'feedback_add.html', context)

def feedback_done(request):
    return render(request, 'feedback_done.html')