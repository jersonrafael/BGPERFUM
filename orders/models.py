from django.db import models
from products.models import *
from accounts.models import *

# Create your models here.
class order(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(product, on_delete=models.CASCADE,default=None)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.client}"