# Generated by Django 3.2.5 on 2021-07-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210727_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_token',
            field=models.CharField(max_length=10, null=True),
        ),
    ]