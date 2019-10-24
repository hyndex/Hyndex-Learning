from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from course.models import *



class CourseReviews(models.Model):
    REVIEW_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    field = models.IntegerField(choices=REVIEW_CHOICES, default=5)
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class LessonReviews(models.Model):
    REVIEW_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5))
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    field = models.IntegerField(choices=REVIEW_CHOICES, default=5)
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)


class CourseEnroll(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Course, on_delete=models.CASCADE)
    completed=models.CharField(max_length=10,blank=True, null=True,default='')
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class LessonUserQuiz(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.PROTECT,blank=True, null=True)
    lesson=models.ForeignKey(Lesson, on_delete=models.PROTECT,blank=True, null=True)
    question=models.ForeignKey(Question, on_delete=models.PROTECT,blank=True, null=True)
    answer=models.ForeignKey(Answer, on_delete=models.PROTECT,blank=True, null=True,default='')
    trial=models.IntegerField(default=0)
    result=models.IntegerField(default=0)
    review=models.TextField(blank=True, null=True,default='')
    time_of_answer=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class GroupCourseAllocation(models.Model):
    course = models.ForeignKey(Course, related_name='groupallocation_course', on_delete=models.PROTECT,blank=True, null=True,default='')
    group = models.ForeignKey(Group, related_name='groupallocation_group', on_delete=models.PROTECT,blank=True, null=True,default='')
    created_by = models.ForeignKey(User, related_name='groupallocation_created_by', on_delete=models.PROTECT,blank=True, null=True,default='')
    deadline = models.DateField(blank=True, null=True,default='')
    date_updated = models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)
#course

#coursequiz

