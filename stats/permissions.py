from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from .models import *

#pk=view.kwargs['id']


class CourseReviewsPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST','GET','PUT','DELETE']:
                # confirm=Institute.objects.filter(user__username=request.user.username).count()>0
                # return confirm
                return True
        return False


def CourseReviewsQuerySet(request):
    corp=Institute.objects.filter(user__username=request.user.username)
    if corp.count()>0:
        if request.method in ['POST','GET','DELETE']:
            return CourseReviews.objects.filter(user__corp__username=request.user.username)
        if request.method == 'PUT':
            return CourseReviews.objects.filter(user__corp__username=request.user.username)

    if request.method in ['POST','PUT','DELETE']:
        return CourseReviews.objects.filter(user__user__username=request.user.username)
    if request.method == 'GET':
        corp=Profile.objects.get(user__username=request.user.username).corp
        return CourseReviews.objects.filter(user__corp__username=corp)


class LessonReviewsPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            # if request.method in ['GET','DELETE','POST','PUT']:
            #     institute=Institute.objects.filter(user__username=request.user.username).count()>0
            #     profile=Profile.objects.filter(user__username=request.user.username).count()>0
            #     if Institute or profile:
            return True
        return False

def LessonReviewsQuerySet(request):
    corp=Institute.objects.filter(user__username=request.user.username)
    if corp.count()>0:
        if request.method in ['GET','DELETE']:
            return LessonReviews.objects.filter(user__corp__username=request.user.username)
        if request.method == 'PUT':
            return LessonReviews.objects.filter(user__user__username=request.user.username)

    if request.method in ['PUT','DELETE']:
        return LessonReviews.objects.filter(user__user__username=request.user.username)
    if request.method == 'GET':
        corp=Profile.objects.get(user__username=request.user.username).corp
        return LessonReviews.objects.filter(user__corp=corp)


class CourseEnrollPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['GET','POST','PUT','DELETE']:
                # confirm=ProfileRole.objects.filter(
                #             Q(user__user__username=request.user.username),
                #             Q(role='admin')|Q(role='groupadmin')).count()>0
                # if confirm:
                return True
        return False

   
def CourseEnrollQuerySet(request):
    corp=Institute.objects.filter(user__username=request.user.username)
    if corp.count()>0:
        if request.method in ['POST','GET','DELETE','PUT']:
            return LessonReviews.objects.filter(user__corp__username=request.user.username)
        
    if request.method in ['GET','POST','PUT','DELETE']:
        return CourseEnroll.objects.filter(user__user__username=request.user.username)



class GroupCourseAllocationPermission(BasePermission):
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

   
def GroupCourseAllocationQuerySet(request):
    corp=Institute.objects.filter(user__username=request.user.username)
    if corp.count()>0:
        if request.method in ['GET','DELETE','PUT']:
            return GroupCourseAllocation.objects.filter(group__corp__user__username=request.user.username)
        
    if request.method in ['GET','POST','PUT','DELETE']:
        corp=Profile.objects.get(user__username=request.user.username).corp
        return GroupCourseAllocation.objects.filter(group__corp=corp)




