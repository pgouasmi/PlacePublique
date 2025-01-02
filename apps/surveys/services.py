import os
import hashlib
import base64
import secrets
import tweepy
from django.shortcuts import redirect
from django.http import HttpResponse
import logging

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

class TwitterService:
   def __init__(self):
       self.code_challenge = secrets.token_urlsafe(64)
       self.oauth2_user_handler = tweepy.OAuth2UserHandler(
           client_id=os.getenv('CLIENT_ID'),
           redirect_uri="http://127.0.0.1:8000/twitter/callback",
           scope=["dm.read"],
           client_secret=os.getenv('CLIENT_SECRET'),
        #    code_challenge=self.code_challenge,
        #    code_challenge_method="plain"
       )

   def get_auth_url(self):
       return self.oauth2_user_handler.get_authorization_url()

   def get_access_token(self, auth_response):
       return self.oauth2_user_handler.fetch_token(
           auth_response,
        #    code_verifier=self.code_challenge
       )