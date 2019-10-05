from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from users.models import *
from media.models import *


class Notification(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE,  related_name='group')
    text_content=models.TextField(blank=True, null=True)
    publish_date=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)
    created_date=models.DateTimeField(default=dt.datetime.now(),blank=True, null=True)

class NotificationMedia(models.Model):
    notification=models.ForeignKey(Notification, on_delete=models.CASCADE)
    media=models.ForeignKey(Media, on_delete=models.PROTECT,blank=True, null=True)

