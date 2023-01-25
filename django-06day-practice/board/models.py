from django.db import models

# Create your models here.

class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.TextField()
    content = models.TextField()
    hit = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.subject}"