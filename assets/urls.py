
from django.conf.urls import url


import assets.views

urlpatterns = [
    url(r'servers/', assets.views.servers_list, name='servers'),
    url(r'server_detail/([0-9a-zA-Z\-]{36})/$', assets.views.server_detail, name='server_detail'),
    url(r'add/', assets.views.server_add, name='server_add'),
    url(r'del/', assets.views.server_del, name='server_del'),
    url(r'update/([0-9a-zA-Z\-]{36})/$', assets.views.server_update, name='server_update'),
]
