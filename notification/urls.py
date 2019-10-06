from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('Notification/',NotificationView.as_view()),
    path('NotificationQuiz/',NotificationQuizView.as_view()),
    path('NotificationMedia/',NotificationMediaView.as_view()),
]
