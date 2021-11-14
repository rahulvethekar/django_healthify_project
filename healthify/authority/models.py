from django.db import models

# Create your models here.


class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Speciality = models.CharField(max_length=50)
    Mobile = models.IntegerField()


class Nurse(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Department = models.CharField(max_length=50)
    Shift = models.CharField(max_length=20)
    Mobile = models.IntegerField()


class RoomService(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Mobile = models.IntegerField()



