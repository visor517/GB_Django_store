from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Category(models.Model):
    name = models.CharField(max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    on_site = CurrentSiteManager('site')

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
    site = models.ManyToManyField(Site)
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return f'{self.name} from {self.arrived_from}'
