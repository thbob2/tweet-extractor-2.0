from celery import Celery
from celery.schedules import crontab

app = Celery('data_extraction', broker='redis://redis:6379/0')

app.conf.beat_schedule = {
    'fetch-tweets-every-hour': {
        'task': 'data_extraction.fetch_tweets',
        'schedule': crontab(minute=0, hour='*'),  # Every hour
    },
}

app.conf.timezone = 'UTC'
