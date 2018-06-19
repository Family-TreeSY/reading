# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class SideBar(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    DISPLAY_TYPE = (
        (1, 'html'),
        (2, '最新图书'),
        (3, '最热阅读'),
    )
    name = models.CharField(max_length=200, verbose_name='名称')
    content = models.CharField(max_length=500, blank=True, verbose_name='内容')
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name='状态'
    )
    display_type = models.PositiveIntegerField(
        default=1, choices=DISPLAY_TYPE, verbose_name='展示类型'
    )
    user = models.ForeignKey(User, verbose_name='管理员')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'

    def __unicode__(self):
        return self.name

    ordering = ['-id']
