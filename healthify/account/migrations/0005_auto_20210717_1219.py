# Generated by Django 3.2.5 on 2021-07-17 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_personalinfo_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Pincode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='Address',
            field=models.CharField(max_length=200),
        ),
    ]
