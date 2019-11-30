from django.db import models
from django.contrib.auth.models import User

class RequestModel(models.Model):
    request_title = models.CharField(max_length=40, null=False, blank=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=False)
    request = models.TextField( null=True, blank=False)
    graphic_type = models.CharField(
        choices= [
        ('Poster', 'Poster'),
        ('Icon', 'Icon'),
        ('Logo', 'Logo'),
        ('Different', 'Different'),
        ], null=False, blank=False,
        max_length=9,
    )
    deadline = models.DateTimeField( null=True, blank=True)
    date_requested = models.DateTimeField(auto_now=True, null=True, blank=True)
    wireframe = models.ImageField(blank=True, null=True,)
    
    
    def __str__(self):
        return self.request_title
        
    def snippet(self):
        return self.request[:150] + '...'
        

class Quote(models.Model):
    owner_request = models.OneToOneField(RequestModel, on_delete=models.CASCADE)
    notes = models.TextField()
    final_product = models.ImageField(blank=True, null=True,)
    designer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_send = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.CharField(
        choices= [
        ('requested', 'requested'),
        ('accepted', 'accepted'),
        ('pending', 'pending'),
        ('rejected', 'rejected'),
        ('delivered', 'delivered'),
        ], null=True, blank=True,
        default="requested",
        max_length=9,
    )
    
    
    def __str__(self):
        return self.status