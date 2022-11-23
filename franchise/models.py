from django.db import models
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    active = models.BooleanField()
    arrival_date = models.DateField(default=datetime.today)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    product_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    manufacture_date = models.DateField(default=datetime.today)
    # time = models.TimeField(default=datetime.now)
    
class Needs(models.Model):
    needs_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    needs_date = models.DateField(default=datetime.today)