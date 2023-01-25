from django.db import models

# Create your models here.
class Book(models.Model):
    site_name = models.CharField(max_length=30)
    site_url = models.TextField()

    def __str__(self):
        return f"{self.site_name}는 {self.site_url} 입니다."