from django.db import models
from django.contrib.sites.models import Site


class Category(models.Model):
    name = models.CharField(max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'Категория {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=64)
    arrived_at = models.DateField()
    price = models.IntegerField()
    unit = models.CharField(max_length=32)
    arrived_from = models.CharField(max_length=64)
    categories = models.ManyToManyField(Category)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} from {self.arrived_from}'
