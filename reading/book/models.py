# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    user = models.ForeignKey(User, verbose_name='使用者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Story(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')
    desc = models.CharField(max_length=200, verbose_name='简述')
    content = models.TextField(verbose_name='详情页')
    image = models.ImageField(max_length=100, verbose_name='图片')
    category = models.ForeignKey(Category, verbose_name='分类')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '书'