from django.db import models

# Create your models here.

class Product(models.Model):
    name        = models.CharField(max_length=30)
    description = models.TextField(max_length=200, default="This is a description of the current item. Descriptions are meant to tell the user more about our products.")
    price       = models.DecimalField(max_digits=5, decimal_places=2)
    image       = models.ImageField(upload_to='images/')
    type = [
        ('M', 'Mens'),
        ('W', 'Womens'),
        ('G', 'Girls'),
        ('B', 'Boys'),
    ]
    category = models.CharField(
        max_length=2,
        choices=type,
    )