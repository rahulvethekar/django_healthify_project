# Generated by Django 3.2.5 on 2021-07-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_Name', models.CharField(max_length=50)),
                ('Patient_Age', models.FloatField()),
                ('Patient_Contact', models.IntegerField()),
                ('Location', models.CharField(max_length=50)),
                ('Reason', models.CharField(max_length=32)),
            ],
        ),
    ]
