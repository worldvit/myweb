from django.db import models

# Create your models here.
class Members(models.Model):
    fname = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=20,null=False)
    phone = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=300,null=False)
    age = models.IntegerField(null=False)
    email = models.EmailField(max_length=100,null=False)
    memo = models.TextField()
    
    def __str__(self):
        return f'{self.lname},{self.fname}'