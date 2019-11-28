from django.conf.urls import url, include
from .views import designs

urlpatterns = [
    url(r'^$', designs, name='designs'),
]