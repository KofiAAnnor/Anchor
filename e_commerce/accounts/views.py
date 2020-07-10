from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from cart.models import Cart

def registerpage_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registerpage.html', {'form': form})

def profile_view(request, *args, **kwargs):
    return render(request, "accounts/profilepage.html", {"quantity": usercartcount(request)})

def usercartcount(request):
    username = request.user.username
    cart = Cart.objects.filter(user=username)
    overallquantity = 0
    for item in cart:
        overallquantity += item.quantity
    return overallquantity