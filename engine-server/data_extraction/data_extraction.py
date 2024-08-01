from celery import Celery
import tweepy
from pymongo import MongoClient
import os

app = Celery('data_extraction', broker='redis://redis:6379/0')

auth = tweepy.OAuth1UserHandler(
    consumer_key=os.getenv('TWITTER_API_KEY'),
    consumer_secret=os.getenv('TWITTER_API_SECRET_KEY'),
    access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)
api = tweepy.API(auth)

client = MongoClient('mongodb://db:27017/')
db = client['tweet_db']

@app.task
def fetch_tweets():
    tweets = api.search_tweets(q='car', count=100, lang='en')
    for tweet in tweets:
        if not db.tweets.find_one({'text': tweet.text, 'created_at': tweet.created_at}):
            db.tweets.insert_one({
                'text': tweet.text,
                'created_at': tweet.created_at,
                'user': tweet.user.screen_name,
                'hashtags': [hashtag['text'] for hashtag in tweet.entities['hashtags']],
                'mentions': [mention['screen_name'] for mention in tweet.entities['user_mentions']]
            })
