# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from assets.models import Servers
import alpha.forms
import json


# 服务器列表
def servers_list(request, number=10):
    servers = Servers.objects.all().order_by('id')
    paginator = Paginator(servers, number)
    page = request.GET.get('page')
    try:
        servers_obj = paginator.page(page)
    except PageNotAnInteger:
        servers_obj = paginator.page(1)
    except EmptyPage:
        servers_obj = paginator.page(paginator.num_pages)
    return render(request, 'assets/servers.html', {'server_list': servers_obj})


# 服务器详情
# 服务器详情页接受GET和POST请求:
# 1.GET请求,返回服务器详情信息
# 2.POST请求,接受form表单数据,写入数据库,返回服务器列表(重定向到服务器列表url)
def server_detail(request, server_id):
    server_obj = Servers.objects.get(id=server_id)
    if request.method == "POST":
        form = alpha.forms.ServersModuleForm(request.POST, instance=server_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/assets/servers')
    else:
        form = alpha.forms.ServersModuleForm(instance=server_obj)
    return render(request, 'assets/server_detail.html', {'server_info': form, 'server_id': server_id})


def server_add(request):
    form = alpha.forms.ServersModuleForm()
    if request.method == "POST":
        form = alpha.forms.ServersModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/assets/servers')
        else:
            return HttpResponseRedirect('/assets/servers')
    else:
        return render(request, 'assets/server_add.html', {'server_field': form})


def server_update(request, server_id):
    if request.method == "POST":
        server_obj = Servers.objects.get(id=server_id)
        form = alpha.forms.ServersModuleForm(request.POST, instance=server_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/assets/servers')
        else:
            print(form.errors)
            return HttpResponseRedirect('/assets/servers')
    else:
        return HttpResponseRedirect('/assets/servers')


# 解决ajax post提交数据出现403
@csrf_exempt
def server_del(request):
    if request.is_ajax():
        # 获取ajax提交来的data
        hostid_obj = request.POST.get('hostid')
        hostid_list = json.loads(hostid_obj)
        for hostid in hostid_list:
            Servers.objects.filter(id=hostid).delete()
        # 定义返回数据,用于ajax回调
        return JsonResponse({'result': 'ok'})
    else:
        return HttpResponseRedirect('/assets/servers')
