from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *


class NotificationStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStatistics
        fields='__all__'
        read_only_fields=('date_updated',)

class NotificationReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationReviews
        fields='__all__'
        read_only_fields=('date_updated',)

class CourseReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReviews
        fields='__all__'
        read_only_fields=('date_updated',)

class LessonReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonReviews
        fields='__all__'
        read_only_fields=('date_updated',)

class LessonEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonEnroll
        fields='__all__'
        read_only_fields=('date_updated',)

class LessonQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonQuiz
        fields='__all__'
        read_only_fields=('date_updated',)

class NotificationQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationQuiz
        fields='__all__'
        read_only_fields=('date_updated',)

