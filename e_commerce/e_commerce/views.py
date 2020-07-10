from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.

def coverpage_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "products/product_list_page.html", {})
    else:
        return render(request, "e_commerce/coverpage.html", {})
