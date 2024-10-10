from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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