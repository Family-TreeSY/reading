# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Category, Story


def book_list(request, category_id=None):
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
        'nav_cates': nav_cates,
        'cates': cates,
    }
    return render(request, 'book/list.html', context=context)


def book_detail(request, pk=None):
    try:
        queryset = Story.objects.get(pk=pk)
    except queryset.DoesNotExist:
        return Http404('Book is not exist!')
    context = {
        'book': queryset,
    }
    return render(request, 'book/detail.html', context=context)
