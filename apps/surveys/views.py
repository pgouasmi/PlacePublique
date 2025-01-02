from django.shortcuts import redirect
from django.http import HttpResponse
from .services import TwitterService
import tweepy
import logging
import os

def twitter_auth(request):
   service = TwitterService()
   auth_url = service.get_auth_url()
   request.session['code_challenge'] = service.code_challenge
   return redirect(auth_url)

def get_messages(request):
   oauth2_user_handler = tweepy.OAuth2UserHandler(
       client_id=os.getenv('CLIENT_ID'),
       redirect_uri="http://127.0.0.1:8000/twitter/callback",
       scope=["dm.read"],
       client_secret=os.getenv('CLIENT_SECRET')
   )
   
   try:
       auth_url = oauth2_user_handler.get_authorization_url()
       print('Please authorize this application: {}'.format(auth_url))

       verifier = input('Enter the authorization response URL:')
    
       return redirect(auth_url)
   except Exception as e:
       logging.error(f"Error getting auth URL: {e}") 
       return HttpResponse("Error in authentication", status=500)

def twitter_callback(request):
   oauth2_user_handler = tweepy.OAuth2UserHandler(
       client_id=os.getenv('CLIENT_ID'),
       redirect_uri="http://127.0.0.1:8000/twitter/callback", 
       scope=["dm.read"],
       client_secret=os.getenv('CLIENT_SECRET')
   )

   try:
       auth_response_url = request.build_absolute_uri()
       token = oauth2_user_handler.fetch_token(auth_response_url)
       client = tweepy.Client(token['access_token'])
       messages = client.get_direct_message_events(user_auth=False)
       
       return JsonResponse({'messages': [msg.text for msg in messages.data]})
   except Exception as e:
       logging.error(f"Error in callback: {e}")
       return HttpResponse(f"Error: {str(e)}", status=500)