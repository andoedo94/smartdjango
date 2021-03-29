import logging

from smartapi.models.models import ValueCharacteristic


class valuecharasteristicServices:

    @classmethod
    def get_value_by_categorie(cls, category_id):
        values = ValueCharacteristic.objects.select_related('key').select_related('value').filter(categorie=category_id)
        return values
