from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from core.forms import FeedbackAddForm
from core.models import Post, PostFavorites, PostComment


def ajax(request):
    return JsonResponse({"status": "Ok", 'message': 'request'})

@login_required
def post_favorite(request, post_id):

    post = Post.objects.get(id=post_id)
    profile = request.user.profile
    PostFavorites.objects.get_or_create(post=post, profile=profile)
    favorites = PostFavorites.objects.filter(post=post).count()

    return JsonResponse({"status": "Ok", 'favorites': favorites})

@login_required
def post_unfavorite(request, post_id):

    post = Post.objects.get(id=post_id)
    profile = request.user.profile
    PostFavorites.objects.filter(post=post, profile=profile).delete()
    favorites = PostFavorites.objects.filter(post=post).count()

    return JsonResponse({"status": "Ok", 'favorites': favorites})


def feedback(request):
    if request.method == "POST":
        form = FeedbackAddForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)


def post_comments(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = PostComment.objects.filter(post=post)

    new_comments = []
    for comment in comments:
        new_comments.append({
            'text': comment.text,
            'profile': comment.profile.user.username
        })
    return JsonResponse({'comments':new_comments}, safe=False)