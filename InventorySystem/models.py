from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Customer(models.Model):
    customerID = models.IntegerField(null=True, blank=True)
    RegistrationDate = models.DateTimeField
    Company = models.CharField(max_length=150)
    ContactName = models.CharField(max_length=20)
    Address = models.CharField(max_length=150)
    PostCode = models.CharField(max_length=20)
    PhoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.Company


class Order(models.Model):
    OrderID = models.IntegerField(null=True, blank=True)
    OrderNumber = models.IntegerField()
    OrderQTY = 
    ProduceID
    CustomerID
    OrderDate


