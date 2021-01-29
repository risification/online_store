from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import OrderForm


# Create your views here.

def products_page(request):
    products = Products.objects.all()
    return render(request, 'products/product.html', {'products': products})


def order_page(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
        form = OrderForm(initial={'product': product})
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products')
        return render(request, 'products/order.html', {'form': form})
    except Products.DoesNotExist:
        return HttpResponse('Not Found')


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


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/order.html', {'form': form})
