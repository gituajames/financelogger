# Generated by Django 5.1.4 on 2025-05-13 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0008_paymentmessages_service_mode_of_payment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile_banking_messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_bank_message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='mode_of_payment',
            field=models.CharField(choices=[('Mpesa', 'Mpesa'), ('KCB', 'KCB'), ('CASH', 'CASH')], max_length=50),
        ),
    ]
