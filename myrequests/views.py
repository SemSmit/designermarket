from django.shortcuts import render
from request.models import RequestModel

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



# class UserAnnouncesList(ListView):
#     model = Announce
#     template_name = 'myApp/user_announces_list.html'
#     context_object_name = 'all_announces_by_user'

#     def get_queryset(self):
#         return Announce.objects.filter(owner=self.kwargs['pk'])