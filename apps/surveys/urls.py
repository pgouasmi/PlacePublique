from django.urls import path
from . import views

urlpatterns = [
    path('twitter/auth/', views.twitter_auth, name='twitter_auth'),
    path('twitter/callback/', views.twitter_callback, name='twitter_callback'),
    path('twitter/messages/', views.get_messages, name='twitter_messages'),
]