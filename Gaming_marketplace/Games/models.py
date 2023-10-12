from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    creator = models.TextField()
    genre = models.TextField()
    year = models.IntegerField()