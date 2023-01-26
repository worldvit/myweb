from django.db import models

# Create your models here.
class gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    memo = models.TextField()
    
    def __str__(self):
        return self.name