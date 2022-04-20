from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from .serializers import QuestionTypeSerializer, PollSerializer, QuestionSerializer, AnswerSerializer, RespondentSerializer, RespondentAnswerSerializer
from .models import QuestionType, Poll, Question, Answer, Respondent, RespondentAnswer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


# Create your views here.


class QuestionTypeList(generics.ListCreateAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    name = 'questiontype-list'
    permission_classes = [IsOwnerOrReadOnly]


class QuestionTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    name = 'questiontype-detail'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    name = 'polls-list'
    permission_classes = [IsOwnerOrReadOnly]


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    name = 'poll-detail'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    name = 'question-list'
    permission_classes = [ IsOwnerOrReadOnly]


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    name = 'question-detail'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    

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

