from django.shortcuts import render
from rest_framework import viewsets
from .models import Tweet, UserProfile
from .serializers import TweetSerializer, UserProfileSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
