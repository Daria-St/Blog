from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.core.serialazers import FeedbackSerialaizer


@api_view(['POST'])
def feedback_rest(request):

    serialaizer = FeedbackSerialaizer(data = request.data)
    serialaizer.is_valid(raise_exception=True)
    serialaizer.save()
    return Response(status=200)

@api_view(['GET'])
def clicks(request):
    return Response({'clicks': 100})