from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile


# Create your views here.
@login_required
def requestview(request):
    current_user = request.user
    if current_user.userprofile.role == "Designer":
        return render(request, "designs.html")
    elif current_user.userprofile.role == "User":
        return render(request, "home.html")
    else: 
        """A view that displays the request page"""
        return render(request, "request.html")
        
