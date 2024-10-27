from rest_framework import serializers

from core.models import Feedback, PostComment


class CommentsSerialaizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=100)
    my_field = serializers.SerializerMethodField(read_only=True)
    profile = serializers.SerializerMethodField()

    def get_my_field(self, obj):
        return 42
    def get_profile(self, obj):
        return obj.profile.user.username

    def create(self, validated_data):
        return PostComment.objects.create(**validated_data)

class FeedbackSerialaizer(serializers.Serializer):
    name = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)