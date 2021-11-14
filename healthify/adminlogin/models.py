from django.db import models

# Create your models here.
class AdminRegister(models.Model):
    username = models.CharField(max_length=10,unique = True)
    password = models.CharField(max_length=10)
