from django.db import models

# Create your models here.

class Phonebook(models.Model):
    fname=models.CharField(max_length=50,null=False)
    lname=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    birthday=models.DateField()