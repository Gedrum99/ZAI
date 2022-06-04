from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet, DateFilter

from rest_framework.reverse import reverse
from .serializers import QuestionTypeSerializer, PollSerializer, QuestionSerializer, AnswerSerializer, RespondentSerializer, RespondentAnswerSerializer, UserPollSerializer
from .models import QuestionType, Poll, Question, Answer, Respondent, RespondentAnswer, User
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


class PollFilter(FilterSet):
    created = DateTimeFilter(field_name='created', lookup_expr='gte')
    class Meta:
        model = Poll
        fields = ['title', 'user', 'created']



class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    name = 'polls-list'
    permission_classes = [IsOwnerOrReadOnly]
    filter_class = PollFilter
    ordering = ['title', 'created']


class UserPollList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    name = 'user-polls'
    serializer_class = UserPollSerializer
    filter_fields = ['username']


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    name = 'poll-detail'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    name = 'question-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    name = 'question-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    name = 'answer-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    name = 'answer-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RespondentList(generics.ListCreateAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    name = 'respondent-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RespondentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    name = 'respondent-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RespondentAnswerList(generics.ListCreateAPIView):
    queryset = RespondentAnswer.objects.all()
    serializer_class = RespondentAnswerSerializer
    name = 'respondent-answer-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RespondentAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespondentAnswer.objects.all()
    serializer_class = RespondentAnswerSerializer
    name = 'respondent-answer-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response({
            'polls': reverse(PollList.name),
            'questions': reverse(QuestionList.name),
            'question-types': reverse(QuestionTypeList.name),
            'question-answers': reverse(AnswerList.name),
            'user-polls': reverse(UserPollList.name),
            'respondents': reverse(RespondentList.name),
            'respondent-answers': reverse(RespondentAnswerList.name)
        })