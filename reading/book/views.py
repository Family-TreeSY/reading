# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Category, Story
from config.models import SideBar


def get_common_context():
    """ 分类
       1、导航分类 nav_cates= Category.objects.filter(is_nav=True)
       2、普通分类 cates = Category.objects.filter(is_nav=False)
   """
    categories = Category.objects.all()
    nav_cates = []
    cates = []
    for category in categories:
        if category.is_nav:
            nav_cates.append(category)
        else:
            cates.append(category)

    sidebar = SideBar.objects.all()
    hot_reading = Story.objects.filter(status=1)[:5]
    recently_book = Story.objects.filter(status=1)[:5]

    context = {
        'nav_cates': nav_cates,
        'cates': cates,
        'sidebars': sidebar,
        'hot_readings': hot_reading,
        'recently_books': recently_book,
    }
    return context


def book_list(request, category_id=None):
    page = request.GET.get('page', 1)
    page_size = 4
    try:
        page = int(page)
    except TypeError:
        page = 1

    queryset = Story.objects.all()
    if category_id:
        queryset = queryset.filter(category_id=category_id)

    paginator = Paginator(queryset, page_size)
    try:
        books = paginator.page(page)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'books': books,
    }
    common_comtext = get_common_context()
    # 把common_context添加到context中
    context.update(common_comtext)
    return render(request, 'book/list.html', context=context)


def book_detail(request, pk=None):
    try:
        queryset = Story.objects.get(pk=pk)
    except queryset.DoesNotExist:
        return Http404('Book is not exist!')
    context = {
        'story': queryset,
    }
    common_context = get_common_context()
    context.update(common_context)
    return render(request, 'book/detail.html', context=context)
