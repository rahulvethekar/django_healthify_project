# Generated by Django 3.2.5 on 2021-07-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210727_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
