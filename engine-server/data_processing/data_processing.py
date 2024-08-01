from celery import Celery
from pymongo import MongoClient
from textblob import TextBlob
import spacy

app = Celery('data_processing', broker='redis://redis:6379/0')

client = MongoClient('mongodb://db:27017/')
db = client['tweet_db']
nlp = spacy.load('en_core_web_sm')

@app.task
def analyze_tweets():
    tweets = db.tweets.find({'score': {'$exists': False}})
    for tweet in tweets:
        text = tweet['text']
        sentiment = TextBlob(text).sentiment.polarity
        doc = nlp(text)
        score = sum(token.vector_norm for token in doc) / len(doc)

        db.tweets.update_one({'_id': tweet['_id']}, {'$set': {'score': score, 'sentiment': sentiment}})
