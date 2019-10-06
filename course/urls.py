from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',CourseView.as_view()),
    path('lesson/',LessonView.as_view()),
    path('question/',LessonQuestionView.as_view()),
    path('grouptocourse/',GroupCourseAllocationView.as_view()),
]
