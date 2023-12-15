import datetime
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Order(models.Model):
    number_Phone = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    oriented = models.CharField(max_length=255)
    commented = models.TextField()
    date_order = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.location
