from django.db import models
from django.contrib.auth.backends import get_user_model
User = get_user_model()

# Create your models here.


class Respondend(models.Model):
    user = models.ForeignKey(User, related_name="respondents", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Respondend no. "+self.user


class Question_type(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Poll(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, related_name="polls", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title + ' '+self.description


class Respondend_answer(models.Model):
    respondend = models.ForeignKey(Respondend, related_name="respondends", on_delete=models.SET_NULL, null=True)
    poll = models.ForeignKey(Poll, related_name="polls", on_delete=models.SET_NULL, null=True)


class Question(models.Model):
    title = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, related_name="questions", on_delete=models.SET_NULL, null=True)
    question_type =models.ForeignKey(Question_type, related_name="questions", on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text