from rest_framework import serializers

from core.models import Feedback


class FeedbackSerialaizer(serializers.Serializer):
    name = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)