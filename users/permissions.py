from rest_framework import permissions
from django.db.models import Q
from .models import *

class CustomGroupPermission(permissions.BasePermission):
    Create=[]
    Update=[]
    Read=[]
    Delete=[]
    def has_permission(self, request, view):
        if request.user.is_authenticated :
            if request.method=='POST':
                if ProfileRole.objects.filter(Q(user__user__username=request.user) & Q(role='admin') | Q(role='groupadmin')).count()>0:
                    return True
        return False
    def has_object_permission(self, request, view):
        if request.user.is_authenticated :
            if request.method=='POST':
                if ProfileRole.objects.filter(Q(user__user__username=request.user) & Q(role='admin') | Q(role='groupadmin')).count()>0:
                    return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated :
            if request.method in 'PUT':
                if ProfileRole.objects.filter(Q(user__user__username=request.user) & Q(role='admin') | Q(role='groupadmin') & Q(group__id=obj.id)).count()>0:
                    return True
            if request.method in 'DELETE':
                if ProfileRole.objects.filter(Q(user__user__username=request.user) & Q(role='admin') | Q(role='groupadmin') & Q(group__id=obj.id)).count()>0:
                    return True
            if request.method in 'GET':
                if ProfileRole.objects.filter(Q(user__user__username=request.user) & Q(group__id=obj.id)).count()>0:
                    return True
        