from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from users.models import *


class ProfileRolePermission(BasePermission):
    message='You are not authorized to this data'
    def has_object_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in ['GET']:
            group_id=request.data['group_id']
            confirm=ProfileRole.objects.filter(user__user__username=request.user.username,
                                        group__id=group_id,
                                        Q(role='admin')||Q(role='groupadmin')).count()
            if not confirm>0:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in ['PUT','DELETE']:
                group_id=request.data['group_id']
                confirm=ProfileRole.objects.filter(user__user__username=request.user.username,
                                        group__id=group_id,
                                        Q(role='admin')||Q(role='groupadmin')).count()
                if confirm>0:
                    return True
            if request.method in ['POST']:
                confirm=Institute.objects.filter(user__username=request.user.username).count()
                if confirm>0:
                    return True
            
        return False

def ProfileRoleQuerySet():
    return ProfileRole.objects.all()

class ProfilePermission(BasePermission):
    message='You are not authorized to this data'
    def has_object_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in ['GET','POST']:
            confirm=Institute.objects.filter(user__username=request.user.username).count()
            if not count>0:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in ['GET','PUT','DELETE']:
                is_Admin=Profile.objects.filter(corp__user__username=request.user.username).count()>0
                is_Self=Profile.objects.filter(user__username=request.user.username).count()>0
                if not is_Admin or is_Self:
                    return False

def ProfileQuerySet():
    return Profile.objects.all()