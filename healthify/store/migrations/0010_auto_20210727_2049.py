# Generated by Django 3.2.5 on 2021-07-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_payment_order_payments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payments',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_token',
            field=models.CharField(blank='', default=0, max_length=10),
            preserve_default=False,
        ),
    ]
