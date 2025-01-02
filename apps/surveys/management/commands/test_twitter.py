from django.core.management.base import BaseCommand
from apps.surveys.services import TwitterService

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        service = TwitterService()
        dms = service.get_dms()
        self.stdout.write(str(dms))