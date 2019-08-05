from django.db import models
from .tasks import make_request

STATUS_CHOICES = [
    ('new', 'New'),
    ('in_process', 'In Process'),
    ('processed', 'Processed'),
]


class WarehouseAccount(models.Model):
    account_name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"


# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=256)
    status = models.CharField(choices=STATUS_CHOICES, max_length=256)
    warehouse_account = models.ForeignKey('WarehouseAccount', on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.order_number, self.status)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pk is not None:
            make_request.delay(order_name=self.order_number, order_status=self.status, order_id=self.pk)

