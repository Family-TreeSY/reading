# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-13 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180613_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name='\u56fe\u7247'),
        ),
    ]