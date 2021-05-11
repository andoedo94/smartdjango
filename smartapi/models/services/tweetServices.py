from django.contrib.gis.geos import Point
from django.db import transaction

from smartapi.models.models import Tweet
from smartapi.models.services.userServices import UserServices


class TweetServices:

    @classmethod
    @transaction.atomic
    def save_tweet(cls, tweet_aux, city):
        user = UserServices.save_user(tweet_aux.user, city)
        tweet = Tweet.objects.filter(tweet_id=tweet_aux.id).first()
        if tweet is None:
            tweet = Tweet()
            tweet.tweet_id = tweet_aux.id
            tweet.user = user
            tweet.city_id = city
            tweet.lang = tweet_aux.lang
            tweet.creation_date = tweet_aux.created_at.date()
            tweet.creation_hour = tweet_aux.created_at.time()
            tweet.text = tweet_aux.text
            if tweet_aux.coordinates is not None:
                tweet.point = Point(tweet_aux.coordinates['coordinates'])
            tweet.save()




