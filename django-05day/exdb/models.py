from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    comment = models.TextField()
    
    # 출력 스트링
    def __str__(self) -> str:
        return f"{self.name} 학생 {self.age} 살"