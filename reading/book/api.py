# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from .models import Story


class StorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    created_time = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S'
    )

    class Meta:
        model = Story
        fields = (
            'name', 'status', 'category', 'author', 'user', 'created_time',
        )


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class UserSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #     slug_field='username',
    #     read_only=True,
    # )

    class Meta:
        model = User
        fields = (
            'id', 'username',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializers_class = UserSerializer
