# Generated by Django 3.1.5 on 2021-01-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210122_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='3424324.png', null=True, upload_to=''),
        ),
    ]
