from django.conf.urls import url, include
from .views import requestview

urlpatterns = [
    url(r'^$', requestview, name='requestview'),
]