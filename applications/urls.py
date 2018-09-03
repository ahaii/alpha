from django.conf.urls import url

import applications.views


urlpatterns = [
    url(r'apps/', applications.views.apps_list, name='apps'),
    url(r'app_detail/([0-9a-zA-Z\-]{36})/$', applications.views.app_detail, name='app_detail'),
    url(r'update/([0-9a-zA-Z\-]{36})/$', applications.views.app_update, name='app_update'),
    url(r'add/', applications.views.app_add, name='app_add'),
    url(r'del/', applications.views.app_del, name='app_del'),
]
