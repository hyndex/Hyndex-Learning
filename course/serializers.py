from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .permissions import *
import datetime as dt



class LessonQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonQuestion
        fields='__all__'
        read_only_fields=('date_updated',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields=('institute','name','description','category','media','thumbnail','instructor','date_updated')
        read_only_fields=('date_updated','institute')

    def create(self, validated_data):
        username = self.context['request'].user.username
        if Institute.objects.filter(user__username=username).count()>0:
            corp = Course.objects.filter(institute__user__username=username)
        else:
            corp = Profile.objects.get(user__username=username).corp.user.username
        institute=institute.objects.get(user__username=institute)
        course = Course.objects.create(institute=institute,**validated_data)
        return course

    def update(self, instance, validated_data):
        course_id = validated_data.pop('course_id')
        course=Course.objects.get(id=course_id)

        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.category=validated_data.get('category',instance.category)
        instance.media=validated_data.get('media',instance.media)
        instance.thumbnail=validated_data.get('thumbnail',instance.thumbnail)
        instance.instructor=validated_data.get('instructor',instance.instructor)
        instance.question_number=validated_data.get('question_number',instance.question_number)
        instance.date_updated=dt.datetime.now()
        instance.save()
        return instance

class LessonSerializer(serializers.ModelSerializer):
    course=CourseSerializer(many=True,write_only=True,source='lessonCourse')
    class Meta:
        model = Lesson
        fields=('course_id','number','name','description','media','thumbnail','question_number','date_updated')
        read_only_fields=('date_updated',)

    def create(self, validated_data):
        course_id = validated_data.pop('course_id')
        course=Course.objects.get(id=course_id)
        lession = Lesson.objects.create(course=course,**validated_data)
        return lession

    def update(self, instance, validated_data):
        course_id = validated_data.pop('course_id')
        course=Course.objects.get(id=course_id)

        instance.number=validated_data.get('number',instance.number)
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.media=validated_data.get('media',instance.media)
        instance.thumbnail=validated_data.get('thumbnail',instance.thumbnail)
        instance.question_number=validated_data.get('question_number',instance.question_number)
        instance.date_updated=dt.datetime.now()
        instance.save()
        return instance


