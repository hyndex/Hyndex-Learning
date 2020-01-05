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
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,blank=True, null=True,default='started')
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)
    updatedtime=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class GroupCourseAllocation(models.Model):
    course = models.ForeignKey(Course, related_name='groupallocationcourse', on_delete=models.PROTECT,blank=True, null=True,default='')
    group = models.ForeignKey(Group, related_name='groupallocationgroup', on_delete=models.PROTECT,blank=True, null=True,default='')
    created_by = models.ForeignKey(User, related_name='groupallocationcreatedby', on_delete=models.PROTECT,blank=True, null=True,default='')
    deadline = models.DateField(blank=True, null=True,default='')
    date_updated = models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)


class LessonPassed(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,blank=True, null=True,default='')#datetimestamp
    visited = models.IntegerField(default=1)
    ip = models.CharField(max_length=10,blank=True, null=True,default='')#datetimestamp
    time=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

    #for ip
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')