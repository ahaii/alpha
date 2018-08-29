# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import assets.models
# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('EIP', 'IIP', 'SystemInfo', 'Mem', 'CPU', 'DataDisk', 'ExpirationDate')
    # 括号中是后台可以展示的字段


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Version', 'InstallDir', 'Status')


admin.site.register(assets.models.Servers, ServerAdmin)
admin.site.register(assets.models.Applications, ApplicationAdmin)
