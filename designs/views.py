from django.shortcuts import render

# Create your views here.
def designs(request):
    """A view that displays the designs page"""
    return render(request, "designs.html")