# Generated by Django 2.2 on 2019-09-25 09:08

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_daily_follow_up', '0006_medication_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='givemedication',
            name='date',
            field=models.DateField(default=datetime.date(2019, 9, 25), verbose_name='Date'),
            preserve_default=False,
        ),
    ]
