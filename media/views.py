from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from .serializers import *


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    # permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    # def get_queryset(self):
    #     return QuestionQuerySet(self.request)