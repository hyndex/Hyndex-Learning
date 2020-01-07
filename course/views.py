from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import FormParser, MultiPartParser,JSONParser, FileUploadParser
from rest_framework.decorators import action
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import datetime as dt



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    search_fields = ['name','category']
    ordering_fields = ['name','category','instructor','date_updated']
    # ordering=('-date_updated',)
    # filter_fields = ['name','category','instructor','institute']
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return CourseQuerySet(self.request)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    search_fields = ['course__name','course__id','name']
    ordering_fields = ['name','number','date_updated']
    ordering=('number',)
    # filter_fields = ['name','number','course__name','course__id','date_updated']
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return LessonQuerySet(self.request)

class CourseUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                instance=Course.objects.get(id=pk)
                up_file  = request.FILES['file']
                instance.media='process'+str(dt.datetime.now())
                instance.original=up_file
                instance.media='done'
                instance.save()
                return Response({"success"},status=204)
            if request.method in ['PUT','DELETE']:
                masterAccount = Institute.objects.filter(user__username=request.user.username)
                admin=ProfileRole.objects.filter(user__user__username=request.user.username,role='admin').count()>0
                if admin or masterAccount.count()>0:
                    if masterAccount.count()>0:
                        instance=Course.objects.get(institute__user__username=request.user.username,id=pk)
                        up_file  = request.FILES['file']
                        up_file.name=str(masterAccount[0].id)+'_'+str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                        instance.media='process'+str(dt.datetime.now())
                        instance.original=up_file
                        instance.media='done'
                        instance.save()
                        return Response({"success"},status=204)
                    else:
                        corp=Profile.objects.get(user__username=request.user.username).corp
                        instance=Course.objects.get(institute__user__username=corp.user.username,id=pk)
                        up_file  = request.FILES['file']
                        up_file.name=str(corp.id)+'_'+str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                        instance.media='process'+str(dt.datetime.now())
                        instance.original=up_file
                        instance.media='done'
                        instance.save()
                        return Response({"success"},status=204)
                else:
                    return Response({"not found"},status=404)

        

class LessonUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                instance=Lesson.objects.get(id=pk)
                up_file  = request.FILES['file']
                instance=Lesson.objects.get(id=pk)
                instance.media='process'+str(dt.datetime.now())
                instance.original=up_file
                instance.media='done'
                instance.save()
                return Response({"success"},status=204)
            if request.method in ['PUT','DELETE']:
                masterAccount = Institute.objects.filter(user__username=request.user.username)
                admin=ProfileRole.objects.filter(user__user__username=request.user.username,role='admin').count()>0
                if admin or masterAccount.count()>0:
                    if masterAccount.count()>0:
                        instance=Lesson.objects.get(course__institute__user__username=request.user.username,id=pk)
                        up_file  = request.FILES['file']
                        up_file.name=str(masterAccount[0].id)+'_'+str(instance.course.id)+'_'+str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                        instance=Lesson.objects.get(id=pk)
                        instance.media='process'+str(dt.datetime.now())
                        instance.original=up_file
                        instance.media='done'
                        instance.save()
                        return Response({"success"},status=204)
                    else:
                        corp=Profile.objects.get(user__username=request.user.username).corp
                        instance=Lesson.objects.get(course__institute__user__username=corp.user.username,id=pk)
                        up_file  = request.FILES['file']
                        up_file.name=str(corp.id)+'_'+str(instance.course.id)+'_'+str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                        instance=Lesson.objects.get(id=pk)
                        instance=Lesson.objects.get(id=pk)
                        instance.media='process'+str(dt.datetime.now())
                        instance.original=up_file
                        instance.media='done'
                        return Response({"success"},status=204)
                else:
                    return Response({"not found"},status=404)
