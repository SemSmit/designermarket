from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def requestview(request):
    """A view that displays the request page"""
    return render(request, "request.html")
        
