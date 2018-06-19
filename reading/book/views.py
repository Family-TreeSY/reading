# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Category, Story


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
