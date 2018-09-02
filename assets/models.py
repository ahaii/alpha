# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import django.utils.timezone as timezone

# Create your models here.
import uuid


product_item = (
    (0, '电商1.0'),
    (1, '电商2.0'),
    (2, '电商3.0'),
    (3, 'NEC'),
    (4, '运维支撑'),
    (5, '大数据')
)


class Servers(models.Model):

    server_status = (
        (0, 'ON'),
        (1, 'OFF'),
    )

    system_info = (
        (0, 'CentOS6.0'),
        (1, 'CentOS6.5'),
        (2, 'CentOS7.0'),
        (4, 'CentOS7.2'),
        (5, 'Windows2008'),
        (6, 'Windows2012'),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    HostName = models.CharField(max_length=20, blank=True, null=True, verbose_name='主机名')
    EIP = models.GenericIPAddressField(blank=True, null=True, verbose_name='公网IP')
    IIP = models.GenericIPAddressField(verbose_name='内网IP')
    Status = models.SmallIntegerField(choices=server_status, default=0, verbose_name='状态')
    SystemInfo = models.SmallIntegerField(choices=system_info, default=0, verbose_name='系统信息')
    Mem = models.IntegerField(default=8, verbose_name='内存')
    CPU = models.IntegerField(default=4)
    SysDisk = models.IntegerField(default=50, verbose_name='系统盘')
    DataDisk = models.IntegerField(default=500, verbose_name='数据盘')
    Applications = models.ManyToManyField('Applications', verbose_name='应用')
    ProductItem = models.SmallIntegerField(choices=product_item, default=6, verbose_name='产品线')
    ExpirationDate = models.DateField(default=timezone.now, verbose_name='到期时间')
    # verbose_name,别名,在admin后台展示时用到

    # python2.x
    def __unicode__(self):
        return self.IIP

    # python3.x
    def __str__(self):
        return self.IIP

    class Meta:
        verbose_name_plural = '服务器'
        # admin中显示的名称


class Applications(models.Model):

    application_status = (
        (0, 'ON'),
        (1, 'OFF'),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    Name = models.CharField(max_length=20, verbose_name='应用名')
    Version = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='版本号')
    InstallDir = models.CharField(max_length=256, verbose_name='安装目录')
    Port = models.IntegerField(verbose_name='端口')
    Status = models.IntegerField(choices=application_status, default=1, verbose_name='状态')
    ProductItem = models.SmallIntegerField(choices=product_item, default=6, verbose_name='产品线')

    # python2.x
    def __unicode__(self):
        return self.Name

    # python3.x
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = '应用'

