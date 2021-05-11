import tweepy as tweepy
from background_task import background

from smartapi.models.services.citiesServices import CitiesService
from smartapi.models.services.tweetServices import TweetServices
from smartcities import settings


@background()
def download_tweets(city_id, initial_date, final_date):
    city = CitiesService.get_city(city_id)
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY_TW, settings.CONSUMER_SECRET_TW)
    auth.set_access_token(settings.ACCESS_TOKEN_TW, settings.ACCESS_TOKEN_SECRET_TW)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    geocode = str(city.latitude) + "," + str(city.longitude) + ",1000mi"
    tweets = tweepy.Cursor(api.search,
                           q="-filter:retweets",
                           geocode=geocode,
                           since=initial_date,
                           until=final_date).items()
    for tweet in tweets:
        TweetServices.save_tweet(tweet, city_id)
