# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def book_list(request, category_id=None):
    context = {
        'name': book_list,
    }
    return render(request, 'book/list.html', context=context)


def book_detail(request, post_id=None):
    context = {
        'name': 'treehl',
    }
    return render(request, 'book/detail.html', context=context)
