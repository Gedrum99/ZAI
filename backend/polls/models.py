from django.db import models
from django.contrib.auth.backends import get_user_model

# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

