import tweepy
from django.conf import settings
from .models import Response, Question
import logging

class TwitterService:
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=settings.TWITTER_API_KEY,
            consumer_secret=settings.TWITTER_API_SECRET,
            access_token=settings.TWITTER_ACCESS_TOKEN,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
        )
        
        logging.info(f"API_KEY: {self.client.consumer_key}\nSECRET_KEY: {self.client.consumer_secret}\nACCESS_TOKEN: {self.client.access_token}\nACCESS_TOKEN_SECRET: {self.client.access_token_secret}")

    def get_dms(self):
        return self.client.get_direct_message_events()