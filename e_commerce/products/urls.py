from django.contrib import admin
from django.urls import path
from .views import productpage_view, menspage_view, womenspage_view, boyspage_view, girlspage_view


app_name = 'products'

urlpatterns = [
    path('', productpage_view, name='productlistpage'),
    path('mens', menspage_view, name='menspage_view'),
    path('womens', womenspage_view, name='womenspage_view'),
    path('girls', girlspage_view, name='girlspage_view'),
    path('boys', boyspage_view, name='boyspage_view'),

]
