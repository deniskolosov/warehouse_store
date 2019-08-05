import os
from store import celery_app
import requests

WAREHOUSE_ORDER_CREATE_URL = os.environ['WAREHOUSE_ORDER_CREATE_URL']


@celery_app.task(bind=True, name='make_request')
def make_request(self, order_status, order_name, order_id):
    data = {
        "order_status": order_status,
        "order_name": order_name,
        "store_order_pk": order_id
    }
    response = requests.post(WAREHOUSE_ORDER_CREATE_URL, json=data)
