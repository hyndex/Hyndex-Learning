from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from users.models import *
from media.models import *
from quiz.models import *



class Notification(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE,  related_name='notification_group')
    title=models.TextField(blank=True, null=True,default='')
    description=models.TextField(blank=True, null=True,default='')
    publish_date=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)
    created_date=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class NotificationMedia(models.Model):
    notification=models.ForeignKey(Notification, related_name='notificationmediaNotification', on_delete=models.CASCADE)
    media=models.ForeignKey(Media, related_name='notificationmediaMedia', on_delete=models.PROTECT,blank=True, null=True,default='')

class NotificationQuiz(models.Model):
    notification=models.ForeignKey(Notification, related_name='notificationquizNotification', on_delete=models.CASCADE)
    quiz=models.ForeignKey(Question, related_name='notificationquiz_quiz', on_delete=models.CASCADE)
    number=models.IntegerField(default=-1,blank=True, null=True)

