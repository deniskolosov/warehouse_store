# Generated by Django 2.2.4 on 2019-08-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='store_order_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
