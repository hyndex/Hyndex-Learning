from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .permissions import *


class CourseReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReviews
        fields=('user','course','field','time')
        read_only_fields=('user','time')
    def create(self, validated_data):
        username = self.context['request'].user.username
        course=validated_data.pop('course')
        field=validated_data.pop('field')
        time=dt.datetime.now()
        review=CourseReviews.objects.filter(course__id=course,user__user__username=username)
        if review.count()>0:
            review=review[0]
            if field >5:
                field=5
            elif field <0:
                field=0
            review.field=field
            review.time=time
            review.save()
            return review
        else:
            course=Course.objects.filter(id=course)
            user=Profile.objects.get(user__username=username)
            return CourseReviews.objects.create(course=course,user=user,field=field,time=time)

class LessonReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonReviews
        fields=('user','lesson','field','time')
        read_only_fields=('user','time')

    def create(self, validated_data):
            username = self.context['request'].user.username
            course=validated_data.pop('course')
            field=validated_data.pop('field')
            time=dt.datetime.now()
            review=CourseReviews.objects.filter(course__id=course,user__user__username=username)
            if review.count()>0:
                review=review[0]
                if field >5:
                    field=5
                elif field <0:
                    field=0
                review.field=field
                review.time=time
                review.save()
                return review
            else:
                course=Course.objects.filter(id=course)
                user=Profile.objects.get(user__username=username)
                return CourseReviews.objects.create(course=course,user=user,field=field,time=time)


class CourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnroll
        fields=('user','course','status','time','updatedtime')
        read_only_fields=('user','time','updatedtime')
        
    def create(self, validated_data):
            username = self.context['request'].user.username
            course=validated_data.pop('course')
            status=validated_data.pop('status')
            time=dt.datetime.now()
            enroll=CourseEnroll.objects.filter(course__id=course,user__user__username=username)
            if enroll.count()==0:
                course=Course.objects.filter(id=course)
                user=Profile.objects.get(user__username=username)
                return CourseEnroll.objects.create(course__id=course,user__user__username=username,status=status,time=dt.datetime.now())

    def update(self, instance, validated_data):
        instance.status=validated_data.pop('status')
        instance.updatedtime=dt.datetime.now()
        instance.save()
        return instance

class LessonPassedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonPassed
        fields=('user','lesson','status','visited','ip','time')
        read_only_fields=('user','time','visited','ip')
        
    def create(self, validated_data):
            ip=self.context['request'].META.get('HTTP_X_FORWARDED_FOR')
            if ip:
                ip = ip.split(',')[0]
            else:
                ip = ip.META.get('REMOTE_ADDR')

            username = self.context['request'].user.username
            lesson=validated_data.pop('lesson')
            status=validated_data.pop('status')
            time=dt.datetime.now()
            lesson=LessonPassed.objects.filter(lesson__id=lesson,user__user__username=username)
            if lesson.count()==0:
                course=Course.objects.filter(id=course)
                user=Profile.objects.get(user__username=username)
                return LessonPassed.objects.create(course__id=course,user__user__username=username,status=status,time=dt.datetime.now(),ip=ip)
            return lesson
    def update(self, instance, validated_data):
        instance.status=validated_data.pop('status')
        instance.time=dt.datetime.now()
        instance.time=1+instance.time
        ip=self.context['request'].META.get('HTTP_X_FORWARDED_FOR')
        if ip:
            ip = ip.split(',')[0]
        else:
            ip = ip.META.get('REMOTE_ADDR')
        instance.time=ip
        instance.save()
        return instance


class GroupCourseAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCourseAllocation
        fields='__all__'
        read_only_fields=('date_updated',)


