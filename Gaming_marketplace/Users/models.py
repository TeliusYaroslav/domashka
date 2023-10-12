from django.db import models

# Create your models here.
class User(models.Model):
    usernamename = models.CharField(max_length = 255)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    password = models.TextField()