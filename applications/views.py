from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from assets.models import Applications
import alpha.forms


def apps_list(request):
    apps_obj = Applications.objects.all().order_by('id')
    return render(request, 'applications/apps.html', {'app_list': apps_obj})


def app_detail(request):
    pass


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






