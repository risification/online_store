# Generated by Django 3.1.5 on 2021-01-22 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210120_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='products_files',
        ),
    ]
