from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

# class User(AbstractUser):
#     pic = models.ImageField()
#     comment = models.TextField()
#     age = models.IntegerField(default=33)
    
#     def getpic(self):
#         if self.pic:
#             return self.pic.url
#         return '/media/noimage.jpg'
