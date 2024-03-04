from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)

    avaliable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class product(models.Model):
    image = models.ImageField(upload_to="static",default=None)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    avaliable = models.BooleanField(default=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE,default=None)

    added_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"