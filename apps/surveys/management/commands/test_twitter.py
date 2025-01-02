# apps/surveys/management/commands/test_twitter.py
from django.core.management.base import BaseCommand
from apps.surveys.services import TwitterService
import tweepy

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            service = TwitterService()
            dms = service.get_dms()
            self.stdout.write(str(dms))
        except tweepy.errors.TweepyException as e:
            self.stdout.write(str(e))
            self.stdout.write(str(e.response.text if hasattr(e, 'response') else 'No response text'))