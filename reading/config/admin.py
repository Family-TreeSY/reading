# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SideBar
from .adminform import SideBarAdminForm
from reading.custom_site import custom_site
from reading.custom_admin import BaseOwnerAdmin


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    form = SideBarAdminForm
    list_display = (
        'name',
        'status',
        'display_type',
        'user',
        'created_time',
    )

    list_filter = (
        'user',
    )

    date_hierarchy = 'created_time'

    fields = (
        'name',
        ('status', 'display_type'),
        'user',
        'content',
    )
