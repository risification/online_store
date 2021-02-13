# Generated by Django 3.1.5 on 2021-02-12 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20210212_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(default=datetime.date(2021, 2, 13)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sale_amount',
            field=models.FloatField(default=0.1),
        ),
    ]
