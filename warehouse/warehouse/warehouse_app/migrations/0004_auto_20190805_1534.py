# Generated by Django 2.2.4 on 2019-08-05 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_app', '0003_auto_20190804_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]