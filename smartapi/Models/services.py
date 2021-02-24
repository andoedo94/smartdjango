from smartapi.Models.models import Citie


class CitiesService:

    @classmethod
    def get_cities(cls):
        cities = Citie.objects.all()
        return cities

