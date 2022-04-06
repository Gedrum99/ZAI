from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from .serializers import QuestionTypeSerializer, PollSerializer, QuestionSerializer, AnswerSerializer, RespondentSerializer, RespondentAnswerSerializer
from .models import QuestionType, Poll, Question, Answer, Respondent, RespondentAnswer

# Create your views here.


class QuestionTypeList(generics.ListCreateAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    name = 'questiontype-list'


class QuestionTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    name = 'questiontype-detail'


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    name = 'polls-list'


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    name = 'poll-detail'


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    name = 'question-list'


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    name = 'question-detail'


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    name = 'answer-list'


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    name = 'answer-detail'


class RespondentList(generics.ListCreateAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    name = 'respondent-list'


class RespondentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    name = 'respondent-detail'

class RespondentAnswerList(generics.ListCreateAPIView):
    queryset = RespondentAnswer.objects.all()
    serializer_class = RespondentAnswerSerializer
    name = 'respondent-answer-list'


class RespondentAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespondentAnswer.objects.all()
    serializer_class = RespondentAnswerSerializer
    name = 'respondent-answer-detail'