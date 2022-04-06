from rest_framework import serializers
from .models import Poll, QuestionType, Question, Answer, Respondent, RespondentAnswer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'user']


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['id', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'poll', 'question_type', 'number']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text','question']

class RespondentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respondent
        fields = ['id','user']

class RespondentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespondentAnswer
        fields = ['id','respondent','poll']
