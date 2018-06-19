# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航分类')
    user = models.ForeignKey(User, verbose_name='管理员')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __unicode__(self):
        return self.name


class Story(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')
    desc = models.CharField(max_length=200, verbose_name='简述')
    content = models.TextField(verbose_name='详情页')
    image = models.ImageField(max_length=100, blank=True, verbose_name='图片')
    category = models.ForeignKey(Category, verbose_name='分类')
    author = models.CharField(max_length=100, verbose_name='作者')
    user = models.ForeignKey(User, verbose_name='管理员')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '图书'
        ordering = ['-id']

    def __unicode__(self):
        return self.name
