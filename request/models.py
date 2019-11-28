from django.db import models
# from accounts.models import UserProfile

class RequestModel(models.Model):
    request_title = models.CharField(max_length=40, null=True, blank=True,)
    
    def __str__(self):
        return self.title
        
        
   