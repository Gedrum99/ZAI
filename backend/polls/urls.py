
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('', views.PollList.as_view(), name=views.PollList.name),
    path('<int:pk>', views.PollDetail.as_view(), name=views.PollDetail.name),

    path('question-type', views.QuestionTypeList.as_view(), name=views.QuestionTypeList.name),
    path('question-type/<int:pk>', views.QuestionTypeDetail.as_view(), name=views.QuestionTypeDetail.name),

    path('question', views.QuestionList.as_view(), name=views.QuestionList.name),
    path('question/<int:pk>', views.QuestionDetail.as_view(), name=views.QuestionDetail.name),
]