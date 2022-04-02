
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('question-type', views.QuestionTypeList.as_view(), name=views.QuestionTypeList.name),
]