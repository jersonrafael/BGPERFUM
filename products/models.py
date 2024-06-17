from django.db import models
from categorys.models import *
# Create your models here.

class discount(models.Model):
    code = models.CharField(max_length=200)
    discount =models.IntegerField()
    activation_date = models.DateTimeField()
    deactivation_date = models.DateTimeField()

    def __str__(self):
        return f"{self.code}"

class product(models.Model):
    image = models.ImageField(upload_to="products/",default=None)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField(default=0)

    discount_code = models.ForeignKey(discount,on_delete=models.CASCADE,default=None, null=True,blank=True)
    avaliable = models.BooleanField(default=True)
    category = models.ForeignKey(category, on_delete=models.SET_NULL,default=None,null=True, blank=True)
    bottle_contend = models.IntegerField(default=0)
    olfactory_family = models.ForeignKey(olfactory_family, on_delete=models.SET_NULL, default=None, null=True, blank=True)

    added_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
