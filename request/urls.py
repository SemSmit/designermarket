from django.conf.urls import url, include
from .views import requestview, make_offer

urlpatterns = [
    url(r'^$', requestview, name='requestview'),
    url(r'^(?P<pk>\d+)/$', make_offer, name='make_offer'),
]