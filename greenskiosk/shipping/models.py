from django.db import models
from shopping.models import Order


# Create your models here.

class ShippingProvider(models.Model):
    name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    transport_mode = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class CoolerBox(models.Model):
    box_number = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=100)
    unlock_code = models.IntegerField()

    def __str__(self):
        return self.location

class Delivery(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    shipping_provider = models.ForeignKey(ShippingProvider,on_delete=models.CASCADE)
    # cooler_box = models.ForeignKey(null,on_delete=CASCADE) using null on the ForeignKey brings an error

    def __str__(self):
        return self.order