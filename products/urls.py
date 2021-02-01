from django.urls import path
from .views import *

urlpatterns = [
    path('', products_page, name='products'),
    path('order/<int:product_id>/', order_page, name='order'),
    path('order_update/<int:order_id>/', update_order, name='order-update'),
    path('order_delete/<int:order_id>/', delete_order, name='order-delete'),
    path('register/', register_page, name='register'),
    path('users/<int:user_id>/', user_page),
    path('description/', description_page, name='about_us'),
    path('contacts/', contacts_page, name='contacts'),
    path('users/<int:user_id>/', user_page, name='user-page'),
    path('login/',login_page, name='login_page'),

]
