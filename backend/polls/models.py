from django.db import models
from django.contrib.auth.backends import get_user_model

# Create your models here.

class Respondend(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return "Respondend no. "+self.id

class Question_type(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Poll(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user_id = models.ForeignKey(User,related_name="users",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title + ' '+self.description

class Respondend_answer(models.Model):
    respondend_id = models.ForeignKey(Respondend, related_name="respondends", on_delete=models.SET_NULL,null=True)
    poll_id = models.ForeignKey(Poll, related_name="polls", on_delete=models.SET_NULL, null=True)

class Question(models.Model):
    title = models.CharField(max_length=100)
    poll_id = models.ForeignKey(Poll,related_name="polls", on_delete=models.SET_NULL,null=True)
    question_type_id =models.ForeignKey(Question_type, related_name="question_types", on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.CharField(max_length=250)
    question_id = models.ForeignKey(Question,related_name="questions",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.text