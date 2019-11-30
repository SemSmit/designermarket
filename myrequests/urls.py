from django.conf.urls import url, include
from .views import myrequests, go_to_request, myoffers, go_to_offer

urlpatterns = [
    url(r'^$', myrequests, name='myrequests'),
    url(r'^(?P<pk>\d+)/$', go_to_request, name='go_to_request'),
    url(r'^my_offers$', myoffers, name='myoffers'),
    url(r'^my_offers/(?P<pk>\d+)/$', go_to_offer, name='go_to_offer'),
]