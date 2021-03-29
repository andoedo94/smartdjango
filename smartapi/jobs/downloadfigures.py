import logging

from smartapi.models.enums import ElementType
from smartapi.models.services.categoriesServices import CategoriesServices
from smartapi.models.services.nodeServices import NodeServices
from smartapi.models.services.relationServices import RelationServices
from smartapi.models.services.valuecharasteristicServices import valuecharasteristicServices
from smartapi.models.services.wayServices import WayServices
from smartapi.utilities.request import request_get
from smartapi.models.services.citiesServices import CitiesService
from smartcities import settings

MAX_SIZE = settings.MAX_SIZE


def download_figures(city_id, category_id, user_id):
    params = {}
    city = CitiesService.get_city(city_id)
    category = CategoriesServices.get_category(category_id)
    values_categories = valuecharasteristicServices.get_value_by_categorie(category_id)
    params["data"] = '[bbox][out:json];' + generate_array(values_categories) + 'out body;'
    params["bbox"] = str(city.left) + ',' + str(city.down) + ',' + str(city.right) + ',' + str(city.up)
    data = request_get(settings.OSM_URL, params)
    if data is not None:
        for element in data["elements"]:
            if element["type"] == ElementType.Node and "tags" in element:
                logging.info("")
                NodeServices.save_node(element, 0, city, category)
            elif element["type"] == ElementType.Way and "tags" in element:
                infonodes = get_partial_info(ElementType.Node, element["nodes"])
                WayServices.save_way(element, 0, city, category, infonodes)
            elif element["type"] == ElementType.Relation and "tags" in element:
                members = list(map(lambda item: item['ref'], element["members"]))
                infoways = get_partial_info(ElementType.Way, members)
                element["members"] = members
                for way in infoways:
                    way['nodesinfo'] = get_partial_info(ElementType.Node, way['nodes'])
                RelationServices.save_relation(element, city, category, infoways)


def generate_array(values_categories):
    array = "("
    for value in values_categories:
        node = 'node["' + value.key.name.lower() + '"="' + value.value.name.lower() + '"];'
        relation = 'rel["' + value.key.name.lower() + '"="' + value.value.name.lower() + '"];'
        way = 'way["' + value.key.name.lower() + '"="' + value.value.name.lower() + '"];'
        array = array + node + relation + way

    array = array + ");"
    return array


def get_element(type, ids):
    params = {"data": '[out:json];(' + type + '(id:' + ids + '););out;'}
    data = request_get(settings.OSM_URL, params)
    return data['elements']


def get_partial_info(type, array):
    infonodes = []
    if len(array) < MAX_SIZE:
        elements = ','.join(map(str, array))
        infonodes = get_element(type, elements)
    else:
        sizenodes = int(len(array) / MAX_SIZE)
        for index in range(sizenodes):
            nodes = array[(index * MAX_SIZE): ((index * MAX_SIZE) + MAX_SIZE)]
            aux = ','.join(map(str, nodes))
            infonodes.extend(get_element(type, aux))
        nodes = array[((index + 1) * MAX_SIZE): len(array)]
        if len(nodes) > 0:
            aux = ','.join(map(str, nodes))
            infonodes.extend(get_element(type, aux))
    return infonodes



