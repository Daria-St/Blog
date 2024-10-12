from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from core.forms import FeedbackAddForm
from core.models import Post, PostFavorites

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