from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import OrderForm


# Create your views here.

def products_page(request):
    products = Products.objects.all()
    return render(request, 'products/product.html', {'products': products})


def order_page(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/order.html', {'form': form})


def register_page(request):
    register = UserCreationForm()
    if request.method == 'POST':
        register = UserCreationForm(request.POST)
        if register.is_valid():
            register.save()
            return redirect('products')
    return render(request, 'products/register.html', {'register': register})


def user_page(request):
    user = User.objects.all()
    return render(request, 'products/user.html', {'user': user})


def description_page(request):
    des = Aboutus.objects.all()
    return render(request, 'products/description.html', {'des': des})


def contacts_page(request):
    cont = Cotancts.objects.all()
    return render(request, 'products/contacts.html', {'cont': cont})
