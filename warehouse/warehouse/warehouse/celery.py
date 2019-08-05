import os
import logging
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')

celery_app = Celery('warehouse_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')


# For this simple project we can use filesystem as broker instead of usual RabbitMQ.
broker_url = os.getenv('CELERY_BROKER_URL', 'filesystem://')
broker_dir = os.getenv('CELERY_BROKER_FOLDER', './broker')

celery_app.conf.update({
    'broker_url': broker_url,
    'broker_transport_options': {
        'data_folder_in': os.path.join(broker_dir, 'out'),
        'data_folder_out': os.path.join(broker_dir, 'out'),
        'data_folder_processed': os.path.join(broker_dir, 'processed')
    },
    'result_persistent': False,
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

logger = logging.getLogger(__name__)


