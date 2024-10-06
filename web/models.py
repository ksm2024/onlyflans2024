import uuid
from django.db import models
from django.contrib.auth.models import User


class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    ingredients = models.TextField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    portion = models.TextField()
    price =  models.DecimalField(max_digits=10, decimal_places=3,default=2.490) 
    stock = models.IntegerField(default=0)
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    
    
    def __str__(self):
        return self.customer_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # -> asocición - relación
    bio = models.TextField(max_length=500, blank=True) # el campo puede estar vacío
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True) # generalmente YYYY-MM-DD (por ejemplo, 2024-08-17).

    def __str__(self):
        return self.user.username
    
