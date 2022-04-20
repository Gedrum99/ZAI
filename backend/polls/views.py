from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from rest_framework import permissions
from .serializers import QuestionTypeSerializer, PollSerializer, QuestionSerializer
from .models import QuestionType, Poll, Question
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
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    name = 'question-detail'