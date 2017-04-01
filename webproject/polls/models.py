#-*- coding: utf-8 -*-
from django.db import models


class Poll(models.Model):
    # auto_increment_id = models.AutoField(primary_key=True,blank=False,null=False)
    question = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll,null=True)
    choice_text = models.CharField(max_length=200,blank=False,null=True)
    votes = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
