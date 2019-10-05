from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from django.db.models import Q
from users.models import *
from media.models import *


class Question(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.ForeignKey(Media, on_delete=models.PROTECT,blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    instructor = models.ForeignKey(Profile,on_delete=models.PROTECT)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)

class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.TextField(blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.ForeignKey(Media, on_delete=models.PROTECT,blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Options, on_delete=models.CASCADE)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)


    
