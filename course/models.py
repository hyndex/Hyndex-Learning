from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from django.db.models import Q
from users.models import *
from media.models import *
from quiz.models import *


class Course(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    category = models.CharField(max_length=50, blank=False, null=True, default = '')
    media = models.ForeignKey(Media, related_name='coursemedia', on_delete=models.PROTECT,blank=True, null=True,default='')
    thumbnail = models.ForeignKey(Media, related_name='thumbnailthumbnail', on_delete=models.PROTECT,blank=True, null=True,default='')
    # status = models.CharField(max_length=10, blank=True, null=True)
    instructor = models.ForeignKey(Profile,on_delete=models.PROTECT)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True, null=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='lessonCourse')
    number = models.IntegerField(blank=False, null=True, default = 0)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.ForeignKey(Media, related_name='lessionmedia', on_delete=models.PROTECT,blank=True, null=True,default='')
    thumbnail = models.ForeignKey(Media, related_name='lessionthumbnail', on_delete=models.PROTECT,blank=True, null=True,default='')
    question_number = models.IntegerField(blank=True, null=True,default=0)
    assignment = models.ForeignKey(Assignment, related_name='lessionassignment', on_delete=models.PROTECT,default='')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True, null=True)

