from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from users.models import *



class Media(models.Model):
    ROLE_CHOICES = (('Public','1'),('Institute','2'),('Group','3'))
    media=models.FileField(upload_to='uploads/Media/')
    name=models.CharField(max_length=50,blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    access=models.CharField(max_length=1, default='2',choices=ROLE_CHOICES)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    uploader=models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,default='')
    publish_date=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)
    created_date=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)
