from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from .models import *

#pk=view.kwargs['id']


class CoursePermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.method == 'POST':
            return True
        if request.user.is_authenticated:
            if request.method in ['GET','PUT','DELETE']:
                confirm=Institute.objects.filter(user__username=request.user.username).count()>0
                return confirm
        return True


def CourseQuerySet(request):
    return Institute.objects.filter(user__username=request.user.username)


class LessonPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['GET','DELETE','POST','PUT']:
                institute=Institute.objects.filter(user__username=request.user.username).count()>0
                profile=Profile.objects.filter(user__username=request.user.username).count()>0
                if (Institute) or (profile and request.method in ['GET','PUT']):
                    return True
        return False

def LessonQuerySet(request):
    if Institute.objects.filter(user__username=request.user.username).count()>0:
        return Profile.objects.filter(corp__user__username=request.user.username)
    return Profile.objects.filter(user__username=request.user.username)


class LessonQuestionPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['GET','POST','PUT','DELETE']:
                confirm=ProfileRole.objects.filter(
                            Q(user__user__username=request.user.username),
                            Q(role='admin')|Q(role='groupadmin')).count()>0
                if confirm:
                    return True
        return False

   
def LessonQuestionQuerySet(request):
    return ProfileRole.objects.filter(
        Q(user__user__username=request.user.username),
        Q(role='admin')|Q(role='groupadmin')
        )




