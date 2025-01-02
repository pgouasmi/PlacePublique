from celery import shared_task
from .services import TwitterService

@shared_task
def fetch_dms():
    service = TwitterService()
    dms = service.get_dms()
    # Logique de traitement
    return len(dms)