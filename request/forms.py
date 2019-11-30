from django import forms
from django.forms import ModelForm
from .models import RequestModel, Quote


class DateInput(forms.DateInput):
    input_type = 'date'

class RequestForm(ModelForm):
    class Meta:
        model = RequestModel
        fields = ['request_title', 'price', 'request', 'graphic_type', 'deadline', 'wireframe']
        widgets = {
            'deadline': DateInput()
        }


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['notes', 'final_product']
