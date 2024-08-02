from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
import os

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_processing.settings')

app = Celery('data_processing')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Set up periodic tasks
app.conf.beat_schedule = {
    'analyze-tweets-every-hour': {
        'task': 'data_processing.analyze_tweets',
        'schedule': crontab(minute=0, hour='*'),  # Every hour
    },
}

app.conf.timezone = 'UTC'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
