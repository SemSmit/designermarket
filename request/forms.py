from django import forms
from django.forms import ModelForm
from .models import RequestModel

class RequestForm(ModelForm):
    class Meta:
        model = RequestModel
        fields = ['request_title', 'price', 'request', 'graphic_type', 'deadline', 'wireframe']
        
