# Generated by Django 3.2.5 on 2021-07-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210724_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='vaccine',
            field=models.CharField(max_length=10),
        ),
    ]
