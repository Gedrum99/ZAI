from rest_framework import serializers
from .models import Poll, QuestionType, Question, Answer, Respondent, RespondentAnswer, User


class PollSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    questions = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='question-detail')

    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'user', 'created', 'questions']


class UserPollSerializer(serializers.ModelSerializer):
    polls = serializers.HyperlinkedRelatedField(many=True, view_name='poll-detail', read_only=True)

    class Meta:
        model = User
        fields = ['username', 'polls']


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['id', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='title')
    question_type = serializers.SlugRelatedField(queryset=QuestionType.objects.all(), slug_field='name')
    answers = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='answer-detail')

    class Meta:
        model = Question
        fields = ['id', 'title', 'poll', 'question_type', 'number', 'answers']


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(queryset=Question.objects.all(),slug_field='title')

    class Meta:
        model = Answer
        fields = ['id', 'text', 'question']


class RespondentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Respondent
        fields = ['id', 'user']


class RespondentAnswerSerializer(serializers.ModelSerializer):
    respondent = serializers.SlugRelatedField(queryset=Respondent.objects.all(),slug_field='user')
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(),slug_field='poll')

    class Meta:
        model = RespondentAnswer
        fields = ['id', 'respondent', 'poll']