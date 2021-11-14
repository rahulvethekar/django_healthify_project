from django.db import models

# Create your models here.
class Appointment(models.Model):
    Patient_Name = models.CharField(max_length = 50)
    Age = models.CharField(max_length = 50)
    Blood_Group = models.CharField(max_length = 50)
    Mobile_No = models.IntegerField()
    Address = models.CharField(max_length=200)
    Appointment_Date = models.DateField()
    Appointment_Time = models.CharField(max_length=56)
    Disease = models.CharField(max_length=50)
    Vaccinated = models.BooleanField()

