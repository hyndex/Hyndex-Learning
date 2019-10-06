from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from media.models import *


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields='__all__'
        read_only_fields=('date_updated',)

class NotificationMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationMedia
        fields='__all__'
        read_only_fields=('date_updated',)

class NotificationQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationQuiz
        fields='__all__'
        read_only_fields=('date_updated',)

class NotificationSerializer(serializers.ModelSerializer):
    media= serializers.ListField(child=serializers.CharField())
    group_id=serializers.IntegerField()
    class Meta:
        model = Notification
        fields=('group_id','title','description','media')
        read_only_fields=('date_updated',)

    def create(self, validated_data):
        media = validated_data.pop('media')
        group_id = validated_data.pop('group_id')
        # media = NotificationMedia.objects.create()
        try:
            #check if person can add in group
            group=Group.objects.filter(id=group_id)
            notification = Notification.objects.create(group=group,**validated_data)
        except Exception as e:
            raise(e)
        
        return notification
    


