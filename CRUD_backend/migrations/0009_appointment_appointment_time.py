# Generated by Django 3.0.5 on 2022-04-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_backend', '0008_remove_appointment_appointment_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
