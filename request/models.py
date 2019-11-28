from django.db import models
from accounts.models import UserProfile

class RequestModel(models.Model):
    request_title = models.CharField(max_length=40, null=True, blank=True,)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True,)
    request = models.TextField(null=True, blank=True,)
    graphic_type = models.CharField(
        choices= [
        ('Poster', 'poster'),
        ('Icon', 'icon'),
        ('Logo', 'logo'),
        ('Different', 'different'),
        ],
        null=True, 
        blank=True,
        max_length=9,
    )
    deadline = models.DateTimeField(auto_now=False, null=True, blank=True,)
    date_requested = models.DateTimeField(auto_now=False, null=True, blank=True,)
    wireframe = models.ImageField(blank=True)
    
    def __str__(self):
        return self.title
        
    def snippet(self):
        return self.request[:50] + '...'
        
    
        
        
   