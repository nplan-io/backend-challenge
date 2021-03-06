""" Celery file """
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge.settings')

app = Celery('challenge')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self, params):
    """ Debugs task """
    print('Request {0!r}: {1}'.format(self.request, params))
    return len(params)
