# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-05 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20180703_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='pv',
            field=models.PositiveIntegerField(default=0, verbose_name='Page_View'),
        ),
        migrations.AddField(
            model_name='story',
            name='uv',
            field=models.PositiveIntegerField(default=0, verbose_name='Unique_Visitor'),
        ),
    ]