from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .permissions import *
import datetime as dt


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=('question','name','description','media')
        read_only_fields=('date_updated','institute')

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=('institute','name','description','media','status','instructor','options')
        read_only_fields=('date_updated','institute')

    def create(self, validated_data):
        username = self.context['request'].user.username
        if Institute.objects.filter(user__username=username).count()>0:
            corp = self.context['request'].user.username
        else:
            corp = Profile.objects.get(user__username=username).corp.user.username
        institute=institute.objects.get(user__username=corp)
        question = Question.objects.create(institute=institute,**validated_data)
        
        options = validated_data.pop('options')
        
        for option in options:
            opt_serializer = Options.objects.create(question=question,
                                    name=option['name'],
                                    description=option['description'],
                                    media=option['media'],
                                    )
        return question

    # def update(self, instance, validated_data):
    #     course_id = validated_data.pop('course_id')
    #     course=Course.objects.get(id=course_id)

    #     instance.number=validated_data.get('number',instance.number)
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.description=validated_data.get('description',instance.description)
    #     instance.media=validated_data.get('media',instance.media)
    #     instance.thumbnail=validated_data.get('thumbnail',instance.thumbnail)
    #     instance.question_number=validated_data.get('question_number',instance.question_number)
    #     instance.date_updated=dt.datetime.now()
    #     instance.save()
    #     return instance