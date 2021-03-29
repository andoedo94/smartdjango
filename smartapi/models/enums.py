from django.db import models


class LinkPlace(models.IntegerChoices):
    TRIPADVISOR = 1
    BOOKING = 2


class ElementType(models.TextChoices):
    Node = 'node'
    Way = 'way'
    Relation = 'relation'


