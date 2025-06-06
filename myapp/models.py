from django.db import models

# Create your models here.
class task(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=150)
    time=models.TimeField(auto_created=True)
    
    def __str__(self):
        return self.title

