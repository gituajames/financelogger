# Generated by Django 5.1 on 2024-10-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finlogger', '0002_rename_description_name_transaction_name_of_recipients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_cost',
            field=models.IntegerField(default=0),
        ),
    ]
