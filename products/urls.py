from django.urls import path
from .views import *

urlpatterns = [
    path('', products_page, name='products'),
    path('order/<int:product_id>/', order_page, name='order'),
    path('order_update/<int:order_id>/', update_order, name='order-update'),
    path('register/', register_page, name='register'),
    path('user/', user_page),
    path('description/', description_page),
    path('contacts/', contacts_page),
]
