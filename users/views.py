from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.authtoken.models import Token
from rest_framework.permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import *

class InstituteView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    model=Institute
    serializer=InstituteSerializer
    queryset = model.objects.all()
    serializer_class = serializer
    lookup_field='id'
    ordering_fields='__all__'
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProfileView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    model=Profile
    serializer=ProfileSerializer
    queryset = model.objects.all()
    serializer_class = serializer
    lookup_field='id'
    #filter_fields='__all__'
    ordering_fields='__all__'
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GroupView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    model=Group
    serializer=GroupSerializer
    queryset = model.objects.all()
    serializer_class = serializer
    lookup_field='id'
    filter_fields='__all__'
    ordering_fields='__all__'
    def post(self, request, *args, **kwargs):
        if not ProfileRole.objects.filter(user__user__username=request.user,role='Admin').count()>0:
            return({'404'})
        return self.create(request, *args, **kwargs)
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ProfileRoleView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    model=ProfileRole
    serializer=ProfileRoleSerializer
    queryset = model.objects.all()
    serializer_class = serializer
    lookup_field='id'
    filter_fields='__all__'
    ordering_fields='__all__'
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)