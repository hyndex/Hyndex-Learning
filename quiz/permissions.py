from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from .models import *

#pk=view.kwargs['id']

class AnswerPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST']:
                id=view.kwargs['id']
                question_id=view.kwargs['question']
                ans=Answer.objects.filter(question__id = question_id,user__user__username = request.user.username).count()>0
                return ans
            if request.method in ['GET']:
                id=view.kwargs['id']
                question_id=view.kwargs['question']
                ans=Answer.objects.filter(user__user__username = request.user.username).count()>0
                return ans
        return False

   
def AnswerQuerySet(request):
    isAdmin =  ProfileRole.objects.filter(
        Q(user__user__username=request.user.username),
        Q(role='admin')|Q(role='groupadmin')
        ).count()>0
    if isAdmin:
        corp = Group.objects.get(corp__user__username=request.user.username).corp
        return Answer.objects.filter(question__institute=corp)
    else:
        corp = Group.objects.get(corp__user__username=request.user.username).corp
        return Answer.objects.filter(question__institute=corp,profile__user__username=request.user.username)
        


