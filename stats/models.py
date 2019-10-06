from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from notification.models import *
from course.models import *


class NotificationStatistics(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    seen=models.CharField(max_length=1,blank=True, null=True,default='1')
    seen_time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)


#check for already exist then update
class NotificationReviews(models.Model):
    REVIEW_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    notification=models.ForeignKey(Notification, on_delete=models.CASCADE)
    field = models.IntegerField(choices=REVIEW_CHOICES, unique=True)
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class CourseReviews(models.Model):
    REVIEW_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    field = models.IntegerField(choices=REVIEW_CHOICES, unique=True)
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class LessonReviews(models.Model):
    REVIEW_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    field = models.IntegerField(choices=REVIEW_CHOICES, unique=True)
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)


class LessonEnroll(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed=models.CharField(max_length=10,blank=True, null=True,default='')
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class LessonQuiz(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.PROTECT,blank=True, null=True)
    lesson=models.ForeignKey(Lesson, on_delete=models.PROTECT,blank=True, null=True)
    question=models.ForeignKey(Question, on_delete=models.PROTECT,blank=True, null=True)
    answer=models.ForeignKey(Answer, on_delete=models.PROTECT,blank=True, null=True,default='')
    trial=models.IntegerField(default=0)
    result=models.IntegerField(default=0)
    review=models.TextField(blank=True, null=True,default='')
    time_of_answer=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class NotificationQuiz(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.PROTECT,blank=True, null=True)
    notification=models.ForeignKey(Notification, on_delete=models.PROTECT,blank=True, null=True)
    question=models.ForeignKey(Question, on_delete=models.PROTECT,blank=True, null=True)
    answer=models.ForeignKey(Answer, on_delete=models.PROTECT,blank=True, null=True,default='')
    trial=models.IntegerField(default=0)
    result=models.IntegerField(default=0)
    review=models.TextField(blank=True, null=True,default='')
    time_of_answer=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

#course

#coursequiz

#notificationquiz
