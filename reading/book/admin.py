# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Story


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status',
        'user',
        'created_time',
    )


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'author',
        'user',
        'created_time'
    )
    list_filter = (
        'author',
    )
    search_fields = [
        'name',
        'category__name',
        'author',
    ]
    date_hierarchy = 'created_time'
    fields = (
        'name',
        ('image', 'category'),
        ('author', 'user'),
        'desc',
        'content',
    )
