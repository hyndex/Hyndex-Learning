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
    media = models.FileField(upload_to='media/course') #models.ForeignKey(Media, related_name='coursemedia', on_delete=models.PROTECT,blank=True, null=True,default='')
    thumbnail = models.FileField(upload_to='media/thumb') #models.ForeignKey(Media, related_name='thumbnailthumbnail', on_delete=models.PROTECT,blank=True, null=True,default='')
    instructor = models.ForeignKey(Profile,on_delete=models.PROTECT,blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True, null=True)
    def __str__(self):
        return (self.institute.user.username+'->'+self.name)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='lessonCourse')
    number = models.IntegerField(blank=False, null=True, default = 0)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.FileField(upload_to='media/lesson')#models.ForeignKey(Media, related_name='lessionmedia', on_delete=models.PROTECT,blank=True, null=True,default='')
    thumbnail = models.ForeignKey(Media, related_name='lessionthumbnail', on_delete=models.PROTECT,blank=True, null=True,default='')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True, null=True)

class AssignmentLesson(models.Model):
    lesson=models.ForeignKey(Lesson, on_delete=models.PROTECT)
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    question_number = models.IntegerField(blank=True, null=True,default=0)
