from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from django.db.models import Q


class Institute(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    phone = models.CharField(max_length=20, blank=False, null=True, default = '')
    address = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=True, default = '')
    phone = models.CharField(max_length=20, blank=False, null=True, default = '')
    address = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='profile/',blank=True, null=True)   
    corp=models.ForeignKey(Institute, on_delete=models.CASCADE,  related_name='profile_owner')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    
    def __str__(self):
        return self.user.username

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile/',blank=True, null=True)
    corp=models.ForeignKey(Institute, on_delete=models.CASCADE,  related_name='group_owner')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)  
    def __str__(self):
        return self.name

class ProfileRole(models.Model):
    ROLE_CHOICES = (('Admin','admin'),('GroupAdmin','groupadmin'),('Employee','employee'))
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.PROTECT, blank=True, null=True,default='')
    role = models.CharField(max_length=15, default='employee',choices=ROLE_CHOICES)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Role_created_by', blank=True,null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Role_updated_by', blank=True,null=True)
    def __str__(self):
        return self.user.user.username+'->'+self.group.name+'('+self.role+')'