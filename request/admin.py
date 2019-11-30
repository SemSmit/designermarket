from django.contrib import admin
from .models import RequestModel, Quote

# Register your models here.

admin.site.register(RequestModel)
admin.site.register(Quote)