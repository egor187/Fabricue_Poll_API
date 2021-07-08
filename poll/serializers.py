from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Poll, Question, Answer


class PollSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=get_user_model().objects.all())

    class Meta:
        model = Poll
        fields = "__all__"


class SelfPollSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=get_user_model().objects.all())

    class Meta:
        model = Poll
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(slug_field="name", queryset=Poll.objects.all())

    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = ["question", "text", "user"]
