# Generated by Django 3.1.5 on 2021-01-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20210129_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotancts',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]