# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import markdown

from django.db import models
from django.db.models import F
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
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name='名称')
    desc = models.CharField(max_length=200, verbose_name='简述')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    pv = models.PositiveIntegerField(default=0, verbose_name='Page_View')
    uv = models.PositiveIntegerField(default=0, verbose_name='Unique_Visitor')
    is_markdown = models.BooleanField(default=True, verbose_name='使用markdown')
    html = models.TextField(default='', verbose_name='html渲染后的页面', help_text='正文可以使用markdown')
    content = models.TextField(verbose_name='详情页')
    image = models.ImageField(max_length=100, blank=True, verbose_name='图片')
    category = models.ForeignKey(Category, verbose_name='分类')
    author = models.CharField(max_length=100, verbose_name='作者')
    user = models.ForeignKey(User, verbose_name='管理员')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def save(self, *args, **kwargs):
        # 覆写save是因为需要对html进行渲染
        if self.is_markdown:
            self.html = markdown.markdown(
                self.content, extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ]
            )
        return super(Story, self).save(*args, **kwargs)

    def increase_pv(self):
        return type(self).objects.filter(id=self.id).update(pv=F('pv') + 1)

    def increase_uv(self):
        return type(self).objects.filter(id=self.id).update(uv=F('uv') + 1)

    class Meta:
        verbose_name = verbose_name_plural = '图书'
        ordering = ['-id']

    def __unicode__(self):
        return self.name
