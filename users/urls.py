from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('Institute/',InstituteView.as_view()),
    path('Profile/',ProfileView.as_view()),
    path('GroupView/',GroupView.as_view()),
    path('ProfileGroupRoleView/',ProfileRoleView.as_view()),
]
