# Generated by Django 3.2.11 on 2022-01-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razorpayapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='razorpay_table',
            name='razorpay_payment_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='razorpay_table',
            name='razorpay_signature',
            field=models.CharField(default='', max_length=200),
        ),
    ]
