# Generated by Django 3.2.16 on 2023-02-01 12:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields
import nobinobi_daily_follow_up.models


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_daily_follow_up', '0001_initial_squashed_0011_auto_20200401_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='NobinobiDailyFollowUpSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_menu', models.BooleanField(default=True, help_text='Requires a restart of the program to see the difference.')),
            ],
            options={
                'verbose_name': 'Nobinobi Daily follow-up Setting',
            },
        ),
    ]
