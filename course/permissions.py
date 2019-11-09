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
        if request.user.is_authenticated:
            if request.method in ['POST','PUT','DELETE']:
                admin=Institute.objects.filter(user__username=request.user.username).count()>0
                groupadmin=ProfileRole.objects.filter(user__user__username=request.user.username , ROLE_CHOICES='groupadmin').count()>0
                if admin  or groupadmin:
                    return True
                else:
                    return False
            if request.method == 'GET':
                confirm=Profile.objects.filter(user__username=request.user.username).count()>0
                return confirm
        return True


def CourseQuerySet(request):
    corp = Profile.objects.get(user__username=request.user.username).corp
    return Course.objects.filter(institute=corp)


class LessonPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST','PUT','DELETE']:
                admin=Institute.objects.filter(user__username=request.user.username).count()>0
                groupadmin=ProfileRole.objects.filter(user__user__username=request.user.username , ROLE_CHOICES='groupadmin').count()>0
                if admin  or groupadmin:
                    return True
                else:
                    return False
            if request.method == 'GET':
                confirm=Profile.objects.filter(user__username=request.user.username).count()>0
                return confirm
        return True

def LessonQuerySet(request):
    corp = Profile.objects.get(user__username=request.user.username).corp
    return Lesson.objects.filter(course__institute=corp)

class LessonQuestionPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST','PUT','DELETE']:
                admin=Institute.objects.filter(user__username=request.user.username).count()>0
                groupadmin=ProfileRole.objects.filter(user__user__username=request.user.username , ROLE_CHOICES='groupadmin').count()>0
                if admin  or groupadmin:
                    return True
                else:
                    return False
            if request.method == 'GET':
                confirm=Profile.objects.filter(user__username=request.user.username).count()>0
                return confirm
        return True

   
def LessonQuestionQuerySet(request):
    corp = Profile.objects.get(user__username=request.user.username).corp
    return LessonQuestion.objects.filter(lession_course__institute=corp)




