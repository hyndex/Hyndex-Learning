from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from django.db.models import Q
from users.models import *
from quiz.models import *


class Course(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    category = models.CharField(max_length=50, blank=False, null=True, default = '')
    media = models.CharField(max_length=200, null=True, blank=True,default='pending')
    original = models.FileField(upload_to='course/',blank=True, null=True)
    media360 = models.FileField(upload_to='course/',blank=True, null=True)
    media720 = models.FileField(upload_to='course/',blank=True, null=True)
    thumbnail = models.CharField(max_length=200, null=True, blank=True,default='')
    instructor = models.ForeignKey(Profile,on_delete=models.PROTECT,blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True, null=True)
    def __str__(self):
        return (self.institute.user.username+'->'+self.name)

    @property
    def lesson(self):
        return self.lesson_set.all().order_by('number')

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField(blank=False, null=True, default = 0)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.CharField(max_length=200, null=True, blank=True,default='')
    original = models.FileField(upload_to='Lesson/',blank=True, null=True)
    media360 = models.FileField(upload_to='Lesson/',blank=True, null=True)
    media720 = models.FileField(upload_to='Lesson/',blank=True, null=True)
    thumbnail = models.CharField(max_length=200, null=True, blank=True,default='')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True, null=True)

class AssignmentLesson(models.Model):
    lesson=models.ForeignKey(Lesson, on_delete=models.PROTECT)
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    question_number = models.IntegerField(blank=True, null=True,default=0)
