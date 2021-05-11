from django.db import transaction

from smartapi.models.models import UserTweet


class UserServices:

    @classmethod
    @transaction.atomic
    def save_user(cls, user_aux, city):
        user = UserTweet.objects.filter(user_id=user_aux.id).first()
        if user is None:
            user = UserTweet()
            user.user_id = user_aux.id
            user.city_id = city
            user.lang = user_aux.lang
            user.location = user_aux.location
            user.time_zone = user_aux.time_zone
            user.save()
        return user
