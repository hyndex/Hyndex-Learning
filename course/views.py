from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from .serializers import *
from rest_framework import filters



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    search_fields = ['name','category','instructor']
    filter_backends = (filters.SearchFilter,)
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return CourseQuerySet(self.request)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    search_fields = ['course__name','course__id','name','']
    filter_backends = (filters.SearchFilter,)
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return LessonQuerySet(self.request)

