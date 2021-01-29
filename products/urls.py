from django.urls import path
from .views import products_page, order_page, register_page, user_page, description_page,contacts_page

urlpatterns = [
    path('', products_page, name='products'),
    path('order/<int:product_id>/', order_page, name='order'),
    path('register/', register_page,name= 'register'),
    path('user/', user_page),
    path('description/', description_page),
    path('contacts/',contacts_page),

]
