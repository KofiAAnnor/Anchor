from django.db import models

# Create your models here.

class Cart(models.Model):
    user        = models.CharField(max_length=100) 
    productid   = models.IntegerField(default=-1)
    product     = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
