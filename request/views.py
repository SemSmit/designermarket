from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from .forms import RequestForm
from myrequests.views import myrequests

# Create your views here.
@login_required
def requestview(request):
    request_form = RequestForm(request.POST)
    if request.method == 'POST':
        if request_form.is_valid():
            x = request_form.save(commit=False)
            x.buyer = request.user
            x.save()
            return myrequests(request)
        else:
            return render(request, "home.html")
    else:
        current_user = request.user
        if current_user.userprofile.role == "Designer":
            return render(request, "designs.html")
        elif current_user.userprofile.role == "User":
            
                
            args = {'request_form': request_form,}
            return render(request, "request.html", args)
        else: 
            """A view that displays the request page"""
            return render(request, "request.html")
        
