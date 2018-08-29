from django.conf.urls import url
import services.views

urlpatterns = [
    url(r'', services.views.index, name='index'),
]