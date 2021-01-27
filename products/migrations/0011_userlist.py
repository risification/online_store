# Generated by Django 3.1.5 on 2021-01-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210124_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, help_text='The first name of the user.', max_length=200)),
                ('last_name', models.CharField(blank=True, help_text='The last name of the user.', max_length=200)),
                ('email', models.EmailField(help_text='The email and username of the user. Required.', max_length=255, unique=True, verbose_name='email address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
