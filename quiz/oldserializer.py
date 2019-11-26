from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from django.db.models import Q
from users.models import *
from media.models import *




class Assignment(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    name = models.TextField(blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.ForeignKey(Media, on_delete=models.PROTECT,related_name='assignmentmedia',blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    def __str__(self):
        return self.name

class Options(models.Model):
    name = models.TextField(blank=False, null=True, default = '')
    # description = models.TextField(blank=False, null=True, default = '')
    # media = models.ForeignKey(Media, on_delete=models.PROTECT,related_name='optionmedia',blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.ForeignKey(Media, on_delete=models.PROTECT,related_name='questionmedia',blank=True, null=True)

    options=models.ManyToManyField(Options)
    ans=models.ForeignKey(Options,on_delete=models.PROTECT,related_name='questionanswer')
    assignment=models.ForeignKey(Assignment,on_delete=models.PROTECT,related_name='questionassignment')
    order = models.SmallIntegerField()

    instructor = models.ForeignKey(Profile,on_delete=models.PROTECT)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)

    def __str__(self):
        return self.name
    


class Answer(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL, blank=True, null=True)
    # option = models.ForeignKey(Options, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    grade = models.FloatField()
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)




##################################

from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .permissions import *
import datetime as dt


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields=('question','name')
        read_only_fields=('date_updated','institute')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields='__all__'#('question','name','description')
        read_only_fields=('date_updated','institute')

class QuestionOptionSerializer(serializers.ModelSerializer):
    answer=serializers.IntegerField(max_value=None, min_value=None)
    class Meta:
        model = Question
        fields=('institute','name','description','media','instructor','options','answer','assignment')
        read_only_fields=('date_updated','institute')

    def create(self, validated_data):
        username = self.context['request'].user.username
        if Institute.objects.filter(user__username=username).count()>0:
            corp = self.context['request'].user.username
        else:
            corp = Profile.objects.get(user__username=username).corp.user.username
        institute=institute.objects.get(user__username=corp)
        
        options = validated_data.pop('options')
        # media = validated_data.pop('media')
        answer = validated_data.pop('answer')
        assignment = validated_data.pop('assignment')
        
        question = Question.objects.create(institute=institute,**validated_data)

        i=1
        for option in options:
            opt_serializer = Options.objects.create(question=question,
                                    name=option['name'],
                                    description=option['description'],
                                    )
            if i == answer:
                ans=opt_serializer
            i = i+1
        question.answer=ans
        question.save()
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


# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields=('question','option','profile','options')
#         read_only_fields=('date_updated','profile')

#     def create(self, validated_data):
#         username = self.context['request'].user.username
#         if Institute.objects.filter(user__username=username).count()>0:
#             corp = self.context['request'].user.username
#         else:
#             corp = Profile.objects.get(user__username=username).corp.user.username
#         institute=institute.objects.get(user__username=corp)
        
#         profile=Profile.objects.get(user__username=username)
#         option = validated_data.pop('options')
#         question = validated_data.pop('question')
        
#         question=Question.objects.get(id=question)
#         option=Options.objects.get(id=option,question=question)
#         answer=Answer.objects.create(question=question,option=option,profile=profile)
        
#         return answer


class AnswerSerializer(serializers.ModelSerializer):
    student = StringSerializer(many=False)

    class Meta:
        model = Answer
        fields = ('__all__')

    def create(self, request):
        data = request.data
        # print(data)

        assignment = Assignment.objects.get(id=data['asntId'])
        profile = Profile.objects.get(user__username=request.user.username)

        graded_asnt = Answer()
        graded_asnt.assignment = assignment
        graded_asnt.student = profile

        questions = [q for q in assignment.questions.all()]
        answers = [data['answers'][a] for a in data['answers']]

        answered_correct_count = 0
        for i in range(len(questions)):
            if questions[i].answer.title == answers[i]:
                answered_correct_count += 1
            i += 1

        grade = answered_correct_count / len(questions) * 100
        graded_asnt.grade = grade
        graded_asnt.save()
        return graded_asnt



    
