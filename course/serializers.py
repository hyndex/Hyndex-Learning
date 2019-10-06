from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *




class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields='__all__'
        read_only_fields=('date_updated',)

class LessonSerializer(serializers.ModelSerializer):
    course=CourseSerializer(many=True,write_only=True,source='lessonCourse')
    class Meta:
        model = Lesson
        fields=('course_id','number','name','description','media','thumbnail','question_number','date_updated')
        read_only_fields=('date_updated',)

class LessonQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LessonQuestion
        fields='__all__'
        read_only_fields=('date_updated',)


class GroupCourseAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCourseAllocation
        fields='__all__'
        read_only_fields=('date_updated',)
