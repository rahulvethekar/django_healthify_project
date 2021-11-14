# Generated by Django 3.2.5 on 2021-07-17 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Blood_Group', models.CharField(max_length=25)),
                ('Mobile_No', models.IntegerField()),
                ('Address', models.TextField()),
                ('Handicapped', models.BooleanField()),
                ('Register', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]