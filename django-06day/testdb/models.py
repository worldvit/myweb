from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    subject = models.CharField(max_length=30)


    def __str__(self):
        return f"{self.age} 살 {self.name} 선생님"