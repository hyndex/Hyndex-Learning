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
    media = models.ForeignKey(Media, related_name='course_media', on_delete=models.PROTECT,blank=True, null=True,default='')
    thumbnail = models.ForeignKey(Media, related_name='thumbnail_thumbnail', on_delete=models.PROTECT,blank=True, null=True,default='')
    # status = models.CharField(max_length=10, blank=True, null=True)
    instructor = models.ForeignKey(Profile,on_delete=models.PROTECT)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True, null=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='lessonCourse')
    number = models.IntegerField(blank=False, null=True, default = 0)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.ForeignKey(Media, related_name='lession_media', on_delete=models.PROTECT,blank=True, null=True,default='')
    thumbnail = models.ForeignKey(Media, related_name='lession_thumbnail', on_delete=models.PROTECT,blank=True, null=True,default='')
    question_number = models.IntegerField(blank=True, null=True,default=0)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True, null=True)

# class LessonMedia(models.Model):
#     lesson=models.ForeignKey(Lesson, related_name='lessonmedia_lesson', on_delete=models.CASCADE)
#     media=models.ForeignKey(Media, related_name='lessonmedia_media', on_delete=models.PROTECT,blank=True, null=True,default='')
#     priority=models.models.IntegerField(default=1)

# class CourseMedia(models.Model):
#     lesson=models.ForeignKey(Course, related_name='coursemedia_lesson', on_delete=models.CASCADE)
#     media=models.ForeignKey(Media, related_name='coursemedia_media', on_delete=models.PROTECT,blank=True, null=True,default='')
#     priority=models.models.IntegerField(default=1)

class LessonQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='lessionquestion_lession', on_delete=models.PROTECT,default='')
    question = models.ForeignKey(Question, related_name='lessionquestion_question', on_delete=models.PROTECT,default='')

class GroupCourseAllocation(models.Model):
    course = models.ForeignKey(Course, related_name='groupallocation_course', on_delete=models.PROTECT,blank=True, null=True,default='')
    group = models.ForeignKey(Group, related_name='groupallocation_group', on_delete=models.PROTECT,blank=True, null=True,default='')
    created_by = models.ForeignKey(User, related_name='groupallocation_created_by', on_delete=models.PROTECT,blank=True, null=True,default='')
    deadline = models.DateField(blank=True, null=True,default='')
    date_updated = models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)


    
