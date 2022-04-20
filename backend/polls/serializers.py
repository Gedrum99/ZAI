from rest_framework import serializers
from .models import Poll, QuestionType, Question


class PollSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'user', 'created']


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['id', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'poll', 'question_type', 'number']
