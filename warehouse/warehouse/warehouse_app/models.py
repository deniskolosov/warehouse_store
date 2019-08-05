from django.db import models
from .tasks import make_request

STATUS_CHOICES = [
    ('new', 'New'),
    ('in_process', 'In Process'),
    ('processed', 'Processed'),
]


class Order(models.Model):
    order_name = models.CharField(max_length=256)
    order_status = models.CharField(max_length=256, choices=STATUS_CHOICES)
    store_order_pk = models.CharField(max_length=256)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):

        # Get older order_status (there can be no order at this point).
        obj = self.__class__._default_manager.filter(pk=self.pk)

        # If order exists and status updated, send update to store.
        if obj and self.order_status != obj.values(
                'order_status').get()['order_status']:
            make_request.delay(order_status=self.order_status,
                               order_name=self.order_name,
                               store_order_id=self.store_order_pk)
        super().save(*args, **kwargs)

