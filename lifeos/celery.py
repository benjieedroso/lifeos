import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lifeos.settings'.replace('OS', 'os'))

app = Celery('lifeos')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()