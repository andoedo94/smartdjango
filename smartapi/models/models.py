from django.db import models

# Create your models here.
from smartapi.models.enums import LinkPlace


class Citie(models.Model):
    name = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=999, decimal_places=999)
    longitude = models.DecimalField(max_digits=999, decimal_places=999)
    left = models.DecimalField(max_digits=999, decimal_places=999)
    down = models.DecimalField(max_digits=999, decimal_places=999)
    right = models.DecimalField(max_digits=999, decimal_places=999)
    up = models.DecimalField(max_digits=999, decimal_places=999)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class LinkCity(models.Model):
    city = models.ForeignKey(Citie, on_delete=models.RESTRICT)
    place = models.IntegerField(choices=LinkPlace.choices)
    value = models.CharField(max_length=150)
