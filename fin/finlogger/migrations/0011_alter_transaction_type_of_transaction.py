# Generated by Django 5.1 on 2024-11-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finlogger', '0010_alter_transaction_type_of_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type_of_transaction',
            field=models.CharField(choices=[('paid', 'Paid'), ('received', 'Received'), ('sent', 'Sent')], max_length=200),
        ),
    ]
