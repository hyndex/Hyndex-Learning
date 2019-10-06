from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('Course/',CourseView.as_view()),
    path('Lesson/',LessonView.as_view()),
    path('Course/',LessonQuestionView.as_view()),
    path('Course/',GroupCourseAllocation.as_view()),
]
