from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from assets.models import Applications
import alpha.forms


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
        form = alpha.forms.ServersModuleForm(instance=app_obj)
    return render(request, 'applications/app_detail.html', {'app_info': form})


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






