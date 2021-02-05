from django.contrib import admin
from .models import *


# Register your models here.
class Product_top(admin.ModelAdmin):
    list_display = ['image', 'name', 'description', 'type', 'price']




admin.site.register(Products, Product_top)
admin.site.register([Order, Aboutus,Profile])

