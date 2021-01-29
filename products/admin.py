from django.contrib import admin
from .models import Products, Order, Aboutus, Cotancts


# Register your models here.
class Product_top(admin.ModelAdmin):
    list_display = ['image', 'name', 'description', 'type', 'price']


class Contacts_top(admin.ModelAdmin):
    list_display = ['contact_type', 'name_user', 'last_name_user', 'phone', 'email', 'address', 'longtitude',
                    'latitude']


admin.site.register(Products, Product_top)
admin.site.register([Order, Aboutus])
admin.site.register(Cotancts, Contacts_top)
