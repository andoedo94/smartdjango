from django.db import transaction

from smartapi.models.models import Relation
from smartapi.models.services.wayServices import WayServices


class RelationServices:

    @classmethod
    @transaction.atomic
    def save_relation(cls, element, city, category, ways):
        relation = Relation.objects.filter(id_relation=element['id']).first()
        if relation is None:
            relation = Relation()
        relation.id_relation = element["id"]
        relation.city = city
        relation.category = category
        if "tags" in element:
            relation.tags = element["tags"]
        relation.save()
        for id in element["members"]:
            way = [item for item in ways if item['id'] == id]
            WayServices.save_way(way[0], relation, city, category, way[0]['nodesinfo'])



