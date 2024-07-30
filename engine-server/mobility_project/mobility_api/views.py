from django.shortcuts import render
from rest_framework import viewsets
from .models import Tweet
from .serializers import TweetSerializer
from django.shortcuts import render
from tweepy import OAuthHandler, API
import os

# Load environment variables
from dotenv import load_dotenv


load_dotenv()

# Twitter API credentials
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = API(auth)

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def fetch_tweets(self):
        tweets = api.search(q='car', count=10)
        for tweet in tweets:
            Tweet.objects.create(
                text=tweet.text,
                created_at=tweet.created_at,
                user_name=tweet.user.name,
                user_handle=tweet.user.screen_name
            )
