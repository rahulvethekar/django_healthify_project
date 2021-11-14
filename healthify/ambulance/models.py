from django.db import models

# Create your models here.
class Ambulance(models.Model):
    Patient_Name = models.CharField(max_length=50)
    Patient_Age = models.FloatField()
    Patient_Contact = models.IntegerField()
    Location = models.CharField(max_length=50)
    Reason = models.CharField(max_length=32)
    Reason = models.CharField(max_length=32 )
    Other = models.CharField(max_length=32 , blank =True )

