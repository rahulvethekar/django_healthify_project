from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PersonalInfo(models.Model):
    Select_Your_User_Id = models.OneToOneField(User,on_delete =models.CASCADE)
    #Full_Name = models.CharField(max_length = 50)
    Gender = models.CharField(max_length=20)
    Age = models.IntegerField()
    Blood_Group = models.CharField(max_length=25)
    Mobile_No = models.IntegerField()
    Address = models.CharField(max_length=200)
    Pincode = models.IntegerField()
    Handicapped = models.BooleanField()


class Appointment(models.Model):
    uid = models.IntegerField()
    first_name = models.CharField(max_length=50 ,null=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.TextField()
    pincode = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    Disease = models.CharField(max_length=50)
    vaccine = models.CharField(max_length=10)

