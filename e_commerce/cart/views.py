from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cart
from products.models import Product

# Create your views here.
def cartpage_view(request, *args, **kwargs):
    username = request.user.username
    cart = Cart.objects.filter(user=username)
    overallquantity = 0
    overalltotal = 0.00
    context = {} 
    context['items'] = []
    for item in cart:
        context['items'].append(item)
        overallquantity += item.quantity
        overalltotal += float(item.product.price * item.quantity)
    overalltotal = "{:.2f}".format(overalltotal)
    context['quantity'] = overallquantity
    context['total'] = overalltotal
    return render(request, "cart/cartpage.html", context)

def addtocart_view(request, *args, **kwargs):
    item_id =  request.POST.get('productid')
    item = Product.objects.get(id=item_id)
    username = request.user.username
    sub_cart = Cart.objects.filter(user=username, productid=item_id)
    if len(sub_cart) == 1:
        sub_cart[0].quantity += 1
        sub_cart[0].save()
    else:
        sub_cart = Cart(user = username,  productid = item_id,  product = item,  quantity = 1)
        sub_cart.save()
    #return render(request, "cart/cartpage.html", {})
    return cartpage_view(request, *args, **kwargs)

def checkout_view(request, *args, **kwargs):
    username = request.user.username
    cart = Cart.objects.filter(user=username).delete()
    overallquantity = 0
    overalltotal = 0.00
    context = {} 
    context['items'] = []    
    context['quantity'] = overallquantity
    context['total'] = overalltotal
    return render(request, "cart/cartpage.html", context)
