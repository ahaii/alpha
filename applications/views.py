from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from assets.models import Applications
import alpha.forms
import json


def apps_list(request):
    apps_obj = Applications.objects.all().order_by('id')
    return render(request, 'applications/apps.html', {'app_list': apps_obj})


def app_detail(request, app_id):
    app_obj = Applications.objects.get(id=app_id)
    if request.method == "POST":
        form = alpha.forms.ApplicationsModuleForm(request.POST, instance=app_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/apps')
    else:
        form = alpha.forms.ApplicationsModuleForm(instance=app_obj)
    return render(request, 'applications/app_detail.html', {'app_info': form, 'app_id': app_id})


def app_update(request, app_id):
    if request.method == "POST":
        app_obj = Applications.objects.get(id=app_id)
        form = alpha.forms.ApplicationsModuleForm(request.POST, instance=app_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/apps')
        else:
            return HttpResponseRedirect('/app/apps')
    else:
        return HttpResponseRedirect('/app/apps')


def app_add(request):
    form = alpha.forms.ApplicationsModuleForm()
    if request.method == "POST":
        form = alpha.forms.ApplicationsModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/apps')
        else:
            return HttpResponseRedirect('/app/apps')
    else:
        return render(request, 'applications/app_add.html', {'app_field': form})


@csrf_exempt
def app_del(request):
    if request.is_ajax():
        # 获取ajax提交来的data
        appid_obj = request.POST.get('appid')
        appid_list = json.loads(appid_obj)
        for appid in appid_list:
            Applications.objects.filter(id=appid).delete()
        # 定义返回数据,用于ajax回调
        return JsonResponse({'result': 'ok'})
    else:
        return HttpResponseRedirect('/app/apps')



