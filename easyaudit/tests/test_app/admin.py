# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from easyaudit.admin import ModelAdminWithHistory
from test_app.models import TestModel


class TestModelAdmin(ModelAdminWithHistory):
    pass


admin.site.register(TestModel, TestModelAdmin)
