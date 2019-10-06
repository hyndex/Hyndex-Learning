from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from media.models import *


class NotificationDireactMediaSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Notification
        fields='__all__'
        read_only_fields=('date_updated',)

