# Generated by Django 5.1 on 2024-10-22 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finlogger', '0004_rename_location_location_of_the_transaction_transaction_geolocation_of_the_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='ammount',
            new_name='amount',
        ),
    ]