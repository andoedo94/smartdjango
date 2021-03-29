from smartapi.models.models import Categories


class CategoriesServices:

    @classmethod
    def get_category(cls, id):
        category = Categories.objects.get(pk=id)
        return category
