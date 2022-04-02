from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from .serializers import QuestionTypeSerializer
from .models import QuestionType

# Create your views here.


class QuestionTypeList(generics.ListCreateAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    name = 'questiontype-list'
