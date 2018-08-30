from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from assets.models import Applications
import alpha.forms


def apps_list(request):
    apps = Applications.objects.all().order_by('id')
    paginator = Paginator(apps, 10)
    page = request.GET.get('page')
    try:
        apps_obj = paginator.page(page)
    except PageNotAnInteger:
        apps_obj = paginator.page(1)
    except EmptyPage:
        apps_obj = paginator.page(paginator.num_pages)
    return render(request, 'apps.html', {'app_list': apps_obj})


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
        return render(request, 'app_add.html', {'app_field': form})