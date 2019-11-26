from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from .models import *

#pk=view.kwargs['id']

class GradedAssignment(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST']:
                id=view.kwargs['id']
                question_id=view.kwargs['question']
                ans=GradedAssignment.objects.filter(question__id = question_id,user__user__username = request.user.username).count()>0
                return ans
            if request.method in ['GET']:
                id=view.kwargs['id']
                question_id=view.kwargs['question']
                ans=GradedAssignment.objects.filter(user__user__username = request.user.username).count()>0
                return ans
        return False

   
def GradedAssignmentQuerySet(request):
    admin=Institute.objects.filter(user__username=request.user.username).count()>0
    if admin:
        queryset=GradedAssignment.objects.filter()
        corp = Group.objects.get(corp__user__username=request.user.username).corp.id
        return GradedAssignment.objects.filter(assignment__institute__id=corp)
    else:
        return GradedAssignment.objects.filter(student__user__username=request.user.username)
        


class AssignmentPermission(BasePermission):
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

def AssignmentQuerySet(request):
    corp=Institute.objects.filter(user__username=request.user.username)
    if corp.count()>0:
        return Assignment.objects.filter(institute__user__username=corp)
    corp=Profile.objects.filter(user__username=request.user.username).corp
    return Assignment.objects.filter(institute__user__username=corp) 
