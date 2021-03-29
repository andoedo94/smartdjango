from django.db import transaction

from smartapi.models.models import Node, WayNode


class NodeServices:

    @classmethod
    @transaction.atomic
    def save_node(cls, element, way, city, category):
        node = Node.objects.filter(id_node=element['id']).first()
        if node is None:
            node = Node()
        node.latitude = element['lat']
        node.longitude = element['lon']
        node.id_node = element['id']
        node.city = city
        node.category = category
        if "tags" in element:
            node.tags = element["tags"]

        node.save()
        if way != 0:
            way_node = WayNode()
            way_node.way = way
            way_node.node = node
            way_node.save()
