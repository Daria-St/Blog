from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.core.serialazers import FeedbackSerialaizer, CommentsSerialaizer
from core.models import PostComment, Post


@api_view(['GET'])
def comments_list_rest(request, post_id):
    comments =PostComment.objects.filter(post__id=post_id)
    serialaizer = CommentsSerialaizer(comments, many=True)
    return Response({'comments':serialaizer.data})

@api_view(['POST'])
def comments_add_rest(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = request.user.profile
    serialaizer = CommentsSerialaizer(data=request.data)
    serialaizer.is_valid(raise_exception=True)

    serialaizer.save(post=post, profile=profile)

    return Response(status=200)

@api_view(['POST'])
def feedback_rest(request):

    serialaizer = FeedbackSerialaizer(data = request.data)
    serialaizer.is_valid(raise_exception=True)
    serialaizer.save()
    return Response(status=200)

@api_view(['GET'])
def clicks(request):
    return Response({'clicks': 100})


@api_view(['GET'])
def comments(request):

    comments = PostComment.objects.all()
    serialaizer = CommentsSerialaizer(comments, many=True)

    return Response({'comments': serialaizer.data})