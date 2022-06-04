
from django.urls import path
from django.urls import include, path
from . import views

# urlpatterns = [
#     # path('polls/', include('polls.urls')),
#     path('', views.PollList.as_view(), name=views.PollList.name),
#     path('<int:pk>', views.PollDetail.as_view(), name=views.PollDetail.name),
#
#     path('question-type', views.QuestionTypeList.as_view(), name=views.QuestionTypeList.name),
#     path('question-type/<int:pk>', views.QuestionTypeDetail.as_view(), name=views.QuestionTypeDetail.name),
#
#     path('question', views.QuestionList.as_view(), name=views.QuestionList.name),
#     path('question/<int:pk>', views.QuestionDetail.as_view(), name=views.QuestionDetail.name),
#
#     path('answer', views.AnswerList.as_view(), name=views.AnswerList.name),
#     path('answer/<int:pk>', views.AnswerDetail.as_view(), name=views.AnswerDetail.name),
#
#     path('respondent', views.RespondentList.as_view(), name=views.RespondentList.name),
#     path('respondent/<int:pk>', views.RespondentDetail.as_view(), name=views.RespondentDetail.name),
#
#     path('respondent-answer', views.RespondentAnswerList.as_view(), name=views.RespondentAnswerList.name),
#     path('respondent-answer/<int:pk>', views.RespondentAnswerDetail.as_view(), name=views.RespondentAnswerDetail.name)
# ]

urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('polls', views.PollList.as_view(), name=views.PollList.name),
    path('polls/<int:pk>', views.PollDetail.as_view(), name=views.PollDetail.name),

    path('user/polls/', views.UserPollList.as_view(), name=views.UserPollList.name),


    path('question-type', views.QuestionTypeList.as_view(), name=views.QuestionTypeList.name),
    path('question-type/<int:pk>', views.QuestionTypeDetail.as_view(), name=views.QuestionTypeDetail.name),

    path('question', views.QuestionList.as_view(), name=views.QuestionList.name),
    path('question/<int:pk>', views.QuestionDetail.as_view(), name=views.QuestionDetail.name),

    path('answer', views.AnswerList.as_view(), name=views.AnswerList.name),
    path('answer/<int:pk>', views.AnswerDetail.as_view(), name=views.AnswerDetail.name),

    path('respondent', views.RespondentList.as_view(), name=views.RespondentList.name),
    path('respondent/<int:pk>', views.RespondentDetail.as_view(), name=views.RespondentDetail.name),

    path('respondent-answer', views.RespondentAnswerList.as_view(), name=views.RespondentAnswerList.name),
    path('respondent-answer/<int:pk>', views.RespondentAnswerDetail.as_view(), name=views.RespondentAnswerDetail.name),

    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]