from django.db import models

# Create your models here.
class Teachers(models.Model):
    lname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    nname = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    memo = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.lname} 선생님'