from django.contrib import admin
from .models import Poll, QuestionType, Question, Answer, Respondent, RespondentAnswer

# Register your models here.
admin.site.register(Poll)
admin.site.register(QuestionType)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Respondent)
admin.site.register(RespondentAnswer)
