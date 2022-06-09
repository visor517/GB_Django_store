from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    arrived_at = models.DateField()
    price = models.IntegerField()
    unit = models.CharField(max_length=32)
    arrived_from = models.CharField(max_length=64)
