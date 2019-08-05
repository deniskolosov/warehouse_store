import os
from warehouse import celery_app
import requests

STORE_ORDER_UPDATE_URL = os.environ['STORE_ORDER_UPDATE_URL']


@celery_app.task(bind=True, name='make_request')
def make_request(self, order_status, order_name, store_order_id):
    response = requests.put(STORE_ORDER_UPDATE_URL + store_order_id,
                            json={"status": order_status,
                                  "order_number": order_name})
