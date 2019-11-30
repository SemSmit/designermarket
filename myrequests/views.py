from django.shortcuts import render
from request.models import RequestModel, Quote

# Create your views here.
    
def myrequests(request):
    """
    A view that gets all requests from this user and sends them
    to myrequests.html
    """
    myrequests = RequestModel.objects.all().filter(buyer_id=request.user)
    return render(request, "myrequests.html", {'myrequests': myrequests})

def go_to_request(request, pk):
    currentrequest = RequestModel.objects.get(pk=pk)
    args = {'currentrequest': currentrequest,}
    return render(request, "currentrequest.html", args)


def myoffers(request):
    """
    A view that gets all offers from this user and sends them
    to myoffers.html
    """
    my_offers = Quote.objects.all().filter(designer=request.user)
    my_offers_get = Quote.objects.all().filter(owner_request__buyer_id=request.user)
    return render(request, "myoffers.html", {'my_offers': my_offers, 'my_offers_get': my_offers_get,})

def go_to_offer(request, pk):
    
    currentoffer = Quote.objects.get(owner_request_id=pk)
    args = {'currentoffer': currentoffer,}
    return render(request, "currentoffer.html", args)