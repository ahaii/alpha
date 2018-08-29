from django.conf.urls import url

import applications.views


urlpatterns = [
    url(r'apps/', applications.views.apps_list, name='apps'),
    url(r'app_detail/', applications.views.app_detail, name='app_detail'),
]