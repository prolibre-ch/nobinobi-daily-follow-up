# Generated by Django 2.2 on 2020-03-25 09:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('nobinobi_daily_follow_up', '0009_fix_early_troubleshoting_relation'),
    ]

    operations = [
        migrations.AddField(
            model_name='presence',
            name='intermediate_arrival_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Intermediate arrival time'),
        ),
        migrations.AddField(
            model_name='presence',
            name='intermediate_departure_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Intermediate departure time'),
        ),
    ]
