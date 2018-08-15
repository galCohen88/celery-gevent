from celery.schedules import crontab
from celery import Celery

__import__('pkg_resources').declare_namespace(__name__)


app = Celery()

app.conf.broker_url = '{host}:{port}/{db}'.format(host='redis://localhost', port=6379, db=0)

# app.conf.broker_transport_options = {'visibility_timeout': 30}

app.conf.beat_schedule = {
    'while_true': {
        'task': 'src.tasks.while_true',
        'schedule': crontab(minute="*/1")
    }
}
