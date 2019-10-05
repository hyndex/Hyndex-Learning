from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    #path('auth/',include('rest_framework.urls')),
    #path('login/',LoginView.as_view()),
    #path('logout/',LogoutView.as_view()),
    path('Institute/',InstituteView.as_view()),
    path('Profile/',ProfileView.as_view()),
    path('GroupView/',GroupView.as_view()),
    path('ProfileGroupRoleView/',ProfileGroupRoleView.as_view()),
]
