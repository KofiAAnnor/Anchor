from django.contrib import admin
from django.urls import include, path
from .views import cartpage_view, addtocart_view, checkout_view


app_name = 'cart'

urlpatterns = [
    path('', cartpage_view, name='cartpage'),    
    path('add', addtocart_view, name='addtocartpage'),    
    path('checkout', checkout_view, name='checkoutpage'),    
]
