from django.db import models

from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField()
    user = models.CharField(max_length=100)
    hashtags = models.CharField(max_length=255, blank=True)
    mentions = models.CharField(max_length=255, blank=True)
    score = models.FloatField(default=0.0)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers_count = models.IntegerField()
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
