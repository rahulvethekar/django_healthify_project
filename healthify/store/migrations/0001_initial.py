# Generated by Django 3.2.5 on 2021-07-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Price', models.FloatField()),
                ('Image', models.ImageField(upload_to='upload/product/image')),
            ],
        ),
    ]
