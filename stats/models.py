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

#reviews

#course

#coursequiz

#notificationquiz
