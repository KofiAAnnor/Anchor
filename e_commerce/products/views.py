from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from cart.models import Cart


# Create your views here.
def productpage_view(request, *args, **kwargs):
    
    return render(request, "products/product_list_page.html", {"quantity": usercartcount(request)})

def menspage_view(request, *args, **kwargs):
    context = {
        "category": "Mens",
        "all_products": Product.objects.filter(category='M'),
        "quantity": usercartcount(request)
    }
    return render(request, "products/product_category_page.html", context)

def womenspage_view(request, *args, **kwargs):
    context = {
        "category": "Womens",
        "all_products": Product.objects.filter(category='W'),
        "quantity": usercartcount(request)
    }
    return render(request, "products/product_category_page.html", context)

def boyspage_view(request, *args, **kwargs):
    context = {
        "category": "Boys",
        "all_products": Product.objects.filter(category='B'),
        "quantity": usercartcount(request)
    }
    return render(request, "products/product_category_page.html", context)

def girlspage_view(request, *args, **kwargs):
    context = {
        "category": "Girls",
        "all_products": Product.objects.filter(category='G'),
        "quantity": usercartcount(request)
    }
    return render(request, "products/product_category_page.html", context)

def usercartcount(request):
    username = request.user.username
    cart = Cart.objects.filter(user=username)
    overallquantity = 0
    for item in cart:
        overallquantity += item.quantity
    return overallquantity