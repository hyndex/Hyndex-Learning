from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .permissions import *


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

class CourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnroll
        fields='__all__'
        read_only_fields=('date_updated',)

class LessonUserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonUserQuiz
        fields='__all__'
        read_only_fields=('date_updated',)

class GroupCourseAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCourseAllocation
        fields='__all__'
        read_only_fields=('date_updated',)


