from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to="static",default=None)

class client(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.email}"