from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class User(AbstractUser):
#     pass
class User(AbstractUser):
    pic = models.ImageField(null=True)
    comment = models.TextField(null=True)
    age = models.IntegerField(null=True)
   
    def getpic(self):
        if self.pic:
            return self.pic.url
        return '/media/noimage.jpg'
    
    def __str__(self):
        return self.username