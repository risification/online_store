from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from e_store.settings import EMAIL_HOST_USER
from .forms import *
import math


# Create your views here.

def products_page(request):
    products = Products.objects.all()
    return render(request, 'products/product.html', {'products': products})


def order_page(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
        total_price = 0
        form = OrderForm(initial={'product': product})
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                total_price = product.price * form.cleaned_data['quantity']
        return render(request, 'products/order.html', {'form': form, 'total_price': total_price})
    except Products.DoesNotExist:
        return HttpResponse('Not Found')


def register_page(request):
    register = UserCreationForm()
    if request.method == 'POST':
        register = UserCreationForm(request.POST)
        if register.is_valid():
            subject = "welcome to our  site!!!"
            body = "Activate your account!"
            from_email = EMAIL_HOST_USER
            to = register.cleaned_data['username']
            message = EmailMessage(subject=subject, body=body, from_email=from_email, to=[to,])
            message.send()
            user = register.save()
            Profile.objects.create(user=user)
            return redirect('products')
    return render(request, 'products/register.html', {'register': register})


def user_page(request, user_id):
    user = User.objects.get(id=user_id)
    orders = user.order_set.all()
    return render(request, 'products/users.html', {'user': user, 'orders': orders})


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
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/order.html', {'form': form})


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('products')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('products')
    return render(request, 'products/login.html')


def logout_page(request):
    logout(request)
    return redirect('/')


def account_settings(request):
    user = request.user.profile
    order_user = request.user
    orders = order_user.order_set.all()
    form = ProfileForm(instance=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {'form': form, 'orders': orders}
    return render(request, 'products/profile.html', context)
