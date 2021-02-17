from django.db import models


# Create your models here.

class Citie(models.Model):

    name = models.CharField(max_length=150)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    left = models.CharField(max_length=20)
    down = models.CharField(max_length=20)
    right = models.CharField(max_length=20)
    up = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    url = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name
