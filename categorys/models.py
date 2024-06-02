from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)
    avaliable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class olfactory_family(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"