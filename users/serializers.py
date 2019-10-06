from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','password','email')
        write_only_fields=('password',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('user','name','phone','address','status','image')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(username=user_data['username'],
                            email=user_data['email'],
                            )
        user.set_password(user_data['password'])
        user.save()
        try:
            profile = Profile.objects.create(user=user,
                                phone=validated_data.pop('phone'),
                                address=validated_data.pop('address'),
                                status=validated_data.pop('status'),
                                image=validated_data.pop('image'),
                                corp= Institute.objects.get(user=self.context['request'].user)
                                )
        except:
            User.objects.filter(username=user_data['username']).delete()
        return profile


class InstituteSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Institute
        fields=('user','name','logo','address','phone')
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(username=user_data['username'],
                            email=user_data['email'],
                            )
        user.set_password(user_data['password'])
        user.save()
        try:
            institute=Institute.objects.create(user=user,
                                logo=validated_data.pop('logo'),
                                address=validated_data.pop('address'),
                                phone=validated_data.pop('phone'),
                                )
        except:
            User.objects.filter(username=user_data['username']).delete()
        return institute

class ProfileRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileRole
        fields='__all__'
        read_only_fields=('date_updated')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields=('name','description','image','corp')
        read_only_fields=('date_updated','corp')

    def create(self, validated_data):
        corp= Institute.objects.get(user=self.context['request'].user)
        institute=Institute.objects.create(corp=corp,**validated_data)
        return institute
