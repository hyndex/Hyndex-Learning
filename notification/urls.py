from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',NotificationView.as_view()),
    path('quiz/',NotificationQuizView.as_view()),
    path('media/',NotificationMediaView.as_view()),
]
