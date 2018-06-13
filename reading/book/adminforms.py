# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django import forms


class StoryAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
