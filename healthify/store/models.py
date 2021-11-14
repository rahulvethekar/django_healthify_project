from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Product(models.Model):
    Category = models.CharField(max_length=50)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.FloatField()
    Image = models.ImageField(upload_to='upload/product/image')



#payment gateway
class Payment(models.Model):
    order_id = models.CharField(max_length=50,null=False)
    payment_id = models.CharField(max_length=50,)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #product = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    # Product order table


class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.FloatField()
    Address = models.CharField(max_length=50)
    Mobile = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    payment_status = models.CharField(max_length=50,default= 'false')
    payment_token = models.CharField(max_length=10)