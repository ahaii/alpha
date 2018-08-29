
from django.conf.urls import url
from django.contrib import admin

import ops.views

urlpatterns = [
    url(r'^/', ops.views.index),
    # url(r'^ssh/([0-9a-zA-Z\-]{36})', ops.views.webssh, name='webssh'),
    # url(r'^ssh/', ops.views.webssh, name='webssh'),
    # url(r'websocket/([0-9a-zA-Z\-]{36})', ops.views.websocket, name='websocket'),
]
