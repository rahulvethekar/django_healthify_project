# Generated by Django 3.2.5 on 2021-07-27 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(default='false', max_length=50),
        ),
    ]