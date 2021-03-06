# coding=utf-8
# Create your models here.
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Poll(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text


class ReceivePolls(models.Model):
    user = models.ForeignKey(User)
    poll = models.ForeignKey(Poll)
    is_answered = models.BooleanField(default=False)
    answer = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.poll.question
