# mobility_api/serializers.py

from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['text', 'created_at', 'user_name', 'user_handle']
