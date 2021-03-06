from django.conf.urls import url, include
from . import urls_reset
from .views import home, register, logout, login
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]