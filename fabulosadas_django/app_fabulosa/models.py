from django.db import models

# Create your models here.
class PropRetos(models.Model):
    username = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=200)
    reto_name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.IntegerField()
    
    def __str__(self):
        return self.reto_name

class Retos(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=200)
    difficulty = models.IntegerField()
    autor = models.TextField(max_length=50)