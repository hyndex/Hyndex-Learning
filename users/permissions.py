from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from users.models import *

#pk=view.kwargs['id']


class InstitutePermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.method == 'POST':
            return True
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                return True
            if request.method in ['GET','PUT','DELETE']:
                masterAccount = Institute.objects.filter(user__username=request.user.username).count()>0
                admin=ProfileRole.objects.filter(user__user__username=request.user.username,role='admin').count()>0
                if admin or masterAccount:
                    return True
        return False


def InstituteQuerySet(request):
    if (request.user.username == 'admin'):
        return Institute.objects.all()
    return Institute.objects.filter(user__username=request.user.username)


class ProfilePermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                return True
            if request.method in ['GET','DELETE','POST','PUT']:
                masterAccount = Institute.objects.filter(user__username=request.user.username).count()>0
                admin=ProfileRole.objects.filter(user__user__username=request.user.username,role='admin').count()>0
                if admin or masterAccount:
                    return True
        return False

def ProfileQuerySet(request):
    if (request.user.username == 'admin'):
        return Profile.objects.all()
    if Institute.objects.filter(user__username=request.user.username).count()>0:
        return Profile.objects.filter(corp__user__username=request.user.username)
    return Profile.objects.filter(user__username=request.user.username)


class ProfileRolePermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                return True
            if request.method in ['GET','POST','PUT','DELETE']:
                masterAccount = Institute.objects.filter(user__username=request.user.username).count()>0
                confirm=ProfileRole.objects.filter(user__user__username=request.user.username,role='admin').count()>0
                if confirm or masterAccount:
                    return True
        return False

   
def ProfileRoleQuerySet(request):
    if (request.user.username == 'admin'):
        return ProfileRole.objects.all()
    masterAccount = Institute.objects.filter(user__username=request.user.username).count()>0
    confirm=ProfileRole.objects.filter(user__user__username=request.user.username,role='admin').count()>0
    if confirm:
        institute = Profile.objects.get(user__username=request.user.username).corp
        return ProfileRole.objects.filter(user__user__username=institute)
    if masterAccount:
        return ProfileRole.objects.filter(user__user__username=request.user.username)
    
    


class GroupPermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                return True
            if request.method in ['GET','POST','PUT','DELETE']:
                masterAccount = Institute.objects.filter(user__username=request.user.username).count()>0
                admin=ProfileRole.objects.filter(user__user__username=request.user.username,role='admin').count()>0
                if admin or masterAccount:
                    return True
            if request.method in ['GET']:
                masterAccount = Institute.objects.filter(user__username=request.user.username).count()>0
                confirm=ProfileRole.objects.filter(user__user__username=request.user.username).count()>0
                if confirm or masterAccount:
                    return True
        return False  

def GroupQuerySet(request):
    if (request.user.username == 'admin'):
        return Group.objects.all()
    try:
        # in case of admin
        institute=Profile.objects.get(user__username=request.user.username).corp.user.username
    except:
        # in case od masterAccount
        institute=request.user.username

    return Group.objects.filter(corp__user__username=institute)

