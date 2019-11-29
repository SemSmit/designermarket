from django.db import models
from django.contrib.auth.models import User

class RequestModel(models.Model):
    request_title = models.CharField(max_length=40, null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    request = models.TextField( null=True, blank=True)
    graphic_type = models.CharField(
        choices= [
        ('Poster', 'Poster'),
        ('Icon', 'Icon'),
        ('Logo', 'Logo'),
        ('Different', 'Different'),
        ], null=True, blank=True,
        max_length=9,
    )
    deadline = models.DateTimeField( null=True, blank=True)
    date_requested = models.DateTimeField(auto_now=True, null=True, blank=True)
    wireframe = models.ImageField(blank=True, null=True,)
    
    def __str__(self):
        return self.request_title
        
    def snippet(self):
        return self.request[:50] + '...'
        
    
        
        
   