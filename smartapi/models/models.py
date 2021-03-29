from django.contrib.postgres.fields import HStoreField
from django.db import models


# Create your models here.
from smartapi.models.enums import LinkPlace


class City(models.Model):
    name = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=30, decimal_places=20)
    longitude = models.DecimalField(max_digits=30, decimal_places=20)
    left = models.DecimalField(max_digits=30, decimal_places=20)
    down = models.DecimalField(max_digits=30, decimal_places=20)
    right = models.DecimalField(max_digits=30, decimal_places=20)
    up = models.DecimalField(max_digits=30, decimal_places=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LinkCity(models.Model):
    place = models.IntegerField(choices=LinkPlace.choices)
    value = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='links')


class Categories(models.Model):
    name = models.CharField(max_length=150)
    priority = models.IntegerField()
    distance = models.IntegerField()


class Characteristic(models.Model):
    name = models.CharField(max_length=150)
    characteristic = models.ForeignKey('self', on_delete=models.CASCADE, related_name='characteristics', null=True)
    isprincipal = models.BooleanField()


class ValueCharacteristic(models.Model):
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categorie')
    key = models.ForeignKey(Characteristic, on_delete=models.CASCADE, related_name='keys')
    value = models.ForeignKey(Characteristic, on_delete=models.CASCADE, related_name='values')


class Relation(models.Model):
    id_relation = models.BigIntegerField()
    tags = HStoreField(null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='citiesrelation')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categoryrelation')
    figure_points = models.CharField(max_length=1000, null=True)


class Way(models.Model):
    id_way = models.BigIntegerField()
    tags = HStoreField(null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='citiesway')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categoryway')
    is_end = models.BooleanField()
    figure_points = models.CharField(max_length=1000, null=True)


class RelationWay(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='relation_way')
    way = models.ForeignKey(Way, on_delete=models.CASCADE)


class Node(models.Model):
    latitude = models.DecimalField(max_digits=30, decimal_places=20)
    longitude = models.DecimalField(max_digits=30, decimal_places=20)
    id_node = models.BigIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='citiesnode')
    tags = HStoreField(null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categorynode')
    figure_points = models.CharField(max_length=1000, null=True)


class WayNode(models.Model):
    way = models.ForeignKey(Way, on_delete=models.CASCADE, related_name='waynode')
    node = models.ForeignKey(Node, on_delete=models.CASCADE)

