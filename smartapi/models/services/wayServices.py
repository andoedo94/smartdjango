from django.db import transaction

from smartapi.models.models import Way, RelationWay
from smartapi.models.services.nodeServices import NodeServices


class WayServices:

    @classmethod
    @transaction.atomic
    def save_way(cls, element, relation, city, category, nodes):
        way = Way.objects.filter(id_way=element['id']).first()
        if way is None:
            way = Way()
        way.id_way = element['id']
        way.city = city
        way.category = category
        if "tags" in element:
            way.tags = element["tags"]
        if element['nodes'][0] == element['nodes'][(len(element['nodes']) - 1)]:
            way.is_end = True
        else:
            way.is_end = False
        way.save()
        for id in element["nodes"]:
            node = [item for item in nodes if item['id'] == id]
            NodeServices.save_node(node[0], way, city, category)

        if relation != 0:
            relation_way = RelationWay()
            relation_way.way = way
            relation_way.relation = relation
            relation_way.save()

