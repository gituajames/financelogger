# Generated by Django 5.1 on 2024-12-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finlogger', '0011_alter_transaction_type_of_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
