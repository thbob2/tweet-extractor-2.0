from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Tweet
from .serializers import TweetSerializer
from django.shortcuts import render
from tweepy import OAuthHandler, API
import os

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
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
