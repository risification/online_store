from django.contrib.auth.models import User
from django.db import models
from datetime import date


# Create your models here.
class Products(models.Model):
    types = (
        ('LAPTOP', 'LAPTOP'),
        ('PHONE', 'PHONE'),
        ('CAR', 'CAR'),
        ('PC', 'PC')
    )
    image = models.ImageField(blank=True, null=True, default='default_product_image.jpg')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    type = models.CharField(choices=types, max_length=20)
    price = models.IntegerField(blank=True, null=True)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}{self.type}{self.price}'


class Order(models.Model):
    p_method = (
        ('money', 'money'),
        ('wallet', 'wallet'),
    )
    statuses = (
        ('In Process', 'In Process'),
        ('Beleivered', 'Belivered'),
        ('Not Belivered', 'Not bdelivered'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default='In products')
    date_created = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=p_method)


class Aboutus(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()


class Cotancts(models.Model):
    contact_type = (
        ('phone', 'phone'),
        ('email', 'email'),
        ('address', 'address')
    )
    contact_type = models.CharField(choices=contact_type, max_length=20)
    name_user = models.CharField(max_length=20)
    last_name_user = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    longtitude = models.IntegerField(blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)


class Profile(models.Model):
    genders = (
        ('F', 'F'),
        ('M', 'M'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='image_suit.png', blank=True, null=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(choices=genders, max_length=20)
    description = models.TextField()
    birth_date = models.DateTimeField(default=date.today())
    twitter_link = models.CharField(max_length=100)
    order_count = models.PositiveIntegerField(default=0)
    wallet = models.PositiveIntegerField(default=0)
    sale_amount = models.FloatField(default=0.1)
