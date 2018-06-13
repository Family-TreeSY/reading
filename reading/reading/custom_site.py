# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_title = 'Reading'
    site_header = 'Reading管理'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
