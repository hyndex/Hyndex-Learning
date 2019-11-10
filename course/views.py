from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from .serializers import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return CourseQuerySet(self.request)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return LessonQuerySet(self.request)

class LessonQuestionViewSet(viewsets.ModelViewSet):
    queryset = LessonQuestion.objects.all()
    serializer_class = LessonQuestionSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return LessonQuestionQuerySet(self.request)

# class GroupCourseAllocationViewSet(viewsets.ModelViewSet):
#     queryset = GroupCourseAllocation.objects.all()
#     serializer_class = GroupCourseAllocationSerializer
#     # permission_classes = [CustomPermission]
#     model=serializer_class().Meta().model
#     def get_queryset(self):
#         return GroupCourseAllocationQuerySet(self.request)