# Generated by Django 3.2.5 on 2021-07-16 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_appointment_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Appointment_date',
            new_name='Appointment_Date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='Appointment_time',
            new_name='Appointment_Time',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='Mobile',
            new_name='Mobile_No',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='Patient_name',
            new_name='Patient_Name',
        ),
    ]
