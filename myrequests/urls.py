from django.conf.urls import url, include
from .views import myrequests

urlpatterns = [
    url(r'^$', myrequests, name='myrequests'),
]