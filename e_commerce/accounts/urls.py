from django.contrib import admin
from django.urls import include, path
from .views import registerpage_view, profile_view
from django.contrib.auth import views as auth_views
from django.conf.urls import url


app_name = 'accounts'

urlpatterns = [
    path('register', registerpage_view, name='registerpage'),    
    path('profile', profile_view, name='profilepage'),    
    path('products/', include('products.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # new
]
