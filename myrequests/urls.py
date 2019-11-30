from django.conf.urls import url, include
from .views import myrequests, go_to_request

urlpatterns = [
    url(r'^$', myrequests, name='myrequests'),
    url(r'^(?P<pk>\d+)/$', go_to_request, name='go_to_request'),
]