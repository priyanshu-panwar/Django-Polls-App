from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse

class Question(models.Model):
    topic = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    date_valid = models.DateField('validity date')

    def __str__(self):
        return self.topic

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=30) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    