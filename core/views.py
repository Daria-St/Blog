from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Post, PostCategory, PostComment, Feedback, PostFavorites
from .forms import PostAddForm, CommentAddForm, FeedbackAddForm, PostAddModelForm

def main(request):
    posts = Post.objects.all()
    category = request.GET.get('category')


    order_by = request.GET.get('order_by')
    page = request.GET.get('page', 1)

    active_category = None


    if category:
        posts = posts.filter(category__id=category)
        active_category = PostCategory.objects.get(id=category)
    if order_by:
        posts = posts.order_by(order_by)

    #логика для пагинации (сколько постов на стринице, несколько страниц и тд)
    # применили метод page, передав туда page - номер страницы
    p = Paginator(posts, 5)
    page_objects = p.page(page)


    categories = PostCategory.objects.all()


    context = {
        "posts": posts,
        'categories': categories,
        'active_category': active_category,
        'page_objects': page_objects
    }

    return render(request, 'main.html', context)

    # return render(request, 'main.html', {"posts": posts})

def post_detail(request, post_id):

    context = {}

    comment_add_form = CommentAddForm()
    post= Post.objects.get(id=post_id)
    comments = PostComment.objects.filter(post=post)

    if request.user.is_authenticated:

        is_favorited = PostFavorites.objects.filter(profile=request.user.profile,
                                                    post=post)
        context.update({'is_favorited':is_favorited})

    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        comment_add_form = CommentAddForm(request.POST)
        if comment_add_form.is_valid():
            data = comment_add_form.cleaned_data
        profile = request.user.profile
        PostComment.objects.create(post=post, text=data['text'], profile=profile)
        return redirect('post_detail', post.id)

    context.update({
        "post": post,
        'comments': comments,
        'comment_add_form': comment_add_form
    })
    return render(request, 'post_detail.html', context)

@login_required
def post_add(request):

    categories = PostCategory.objects.all()
    post_add_form = PostAddModelForm()

    if request.method == "POST":
        post_add_form = PostAddModelForm(request.POST)
        if post_add_form.is_valid():
        #     data = post_add_form.cleaned_data
        #
        #     profile = request.user.profile
        #     Post.objects.create(title=data['title'],
        #                         text=data['text'],
        #                         category=data['category'],
        #                         profile=profile)
            post = post_add_form.save(commit = False)
            profile = request.user.profile
            post.profile = profile
            post.save()

            return redirect('main')

    context = {
        'categories':categories,
        'post_add_form':post_add_form
    }
    return render(request, 'post_add.html', context)


@login_required
def post_edit(request, post_id):

    post = Post.objects.get(id=post_id)
    if post.profile != request.user.profile:
        raise Http404
    form = PostAddModelForm(instance=post)

    if request.method == 'POST':
        form = PostAddModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post.id)

    return render(request, 'post_edit.html', {"post_add_form":form})

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


@login_required
def post_favorite(request, post_id):

    redirect_url = request.GET.get('next')
    post = Post.objects.get(id=post_id)
    profile = request.user.profile
    PostFavorites.objects.get_or_create(post=post, profile=profile)

    return redirect(redirect_url)

@login_required
def post_unfavorite(request, post_id):

    redirect_url = request.GET.get('next')
    post = Post.objects.get(id=post_id)
    profile = request.user.profile
    PostFavorites.objects.filter(post=post, profile=profile).delete()

    return redirect(redirect_url)