# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-19 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20180619_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '\u6b63\u5e38'), (2, '\u5220\u9664')], default=1, verbose_name='\u72b6\u6001'),
        ),
    ]