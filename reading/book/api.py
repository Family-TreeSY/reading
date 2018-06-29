# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from .models import Story, Category


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
            'url', 'name', 'status', 'category', 'author', 'user', 'created_time',
        )


class StoryDetailSerializer(serializers.ModelSerializer):
    stories = StorySerializer(
        read_only=True,
    )

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Story
        fields = (
            'id', 'name', 'user', 'desc', 'stories',
        )


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = StoryDetailSerializer
        return super(StoryViewSet, self).retrieve(request, *args, **kwargs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializers_class = UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    created_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
    )

    class Meta:
        model = Category
        fields = (
            'url', 'name', 'status', 'is_nav', 'user', 'created_time',
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    story_set = StorySerializer(
        many=True,
        read_only=True,
    )

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'user', 'story_set',
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=1)
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super(CategoryViewSet, self).retrieve(request, *args, **kwargs)
