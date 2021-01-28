from django.db import models


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

    def __str__(self):
        return f'{self.name}{self.type}{self.price}'


class Order(models.Model):
    statuses = (
        ('In Process', 'In Process'),
        ('Beleivered', 'Belivered'),
        ('Not Belivered', 'Not bdelivered'),
    )
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default='In products')
    date_created = models.DateTimeField(auto_now_add=True)


class Aboutus(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()


class Cotancts(models.Model):
    name_user = models.CharField(max_length=20,blank=True,null=True)
    last_name_user = models.CharField(max_length=20,blank=True,null=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=50,blank=True,null=True)
