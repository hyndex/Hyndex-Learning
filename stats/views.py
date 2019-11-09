from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from .serializers import *


class CourseReviewsViewSet(viewsets.ModelViewSet):
    queryset = CourseReviews.objects.all()
    serializer_class = CourseReviewsSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return CourseReviewsQuerySet(self.request)

class LessonReviewsViewSet(viewsets.ModelViewSet):
    queryset = LessonReviews.objects.all()
    serializer_class = LessonReviewsSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return LessonReviewsQuerySet(self.request)

class CourseEnrollViewSet(viewsets.ModelViewSet):
    queryset = CourseEnroll.objects.all()
    serializer_class = CourseEnrollSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return CourseEnrollQuerySet(self.request)

class LessonUserQuizViewSet(viewsets.ModelViewSet):
    queryset = LessonUserQuiz.objects.all()
    serializer_class = LessonUserQuizSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return LessonUserQuizQuerySet(self.request)

class GroupCourseAllocationViewSet(viewsets.ModelViewSet):
    queryset = GroupCourseAllocation.objects.all()
    serializer_class = GroupCourseAllocationSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return GroupCourseAllocationQuerySet(self.request)