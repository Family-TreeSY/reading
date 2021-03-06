# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Story
from reading.custom_site import custom_site
from .adminforms import StoryAdminForm
from reading.custom_admin import BaseOwnerAdmin


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = (
        'name',
        'status',
        'user',
        'is_nav',
        'created_time',
        'operator',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:book_category_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(Story, site=custom_site)
class StoryAdmin(BaseOwnerAdmin):
    form = StoryAdminForm
    list_display = (
        'name',
        'category',
        'is_markdown',
        'author',
        'user',
        'pv',
        'uv',
        'created_time',
        'operator',
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
        'status',
        ('image', 'category'),
        ('author', 'user'),
        'desc',
        ('content', 'is_markdown'),
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:book_story_change', args=(obj.id,))
        )
    operator.short_description = '操作'
