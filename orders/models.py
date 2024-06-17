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


class sale(models.Model):
    product = models.ForeignKey(product,default=None,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.product.price
        super(sale, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} - {self.quantity}"