from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imageSRC = models.CharField(max_length=1000)
    quantity_available = models.PositiveIntegerField(default=10)


class Cart(models.Model):
    products = models.ManyToManyField('Product')
    def total_price(self):
        return self.products.aggregate(total_price=models.Sum('price')).get('total_price') or 0


class Wishlist(models.Model):
    products = models.ManyToManyField('Product')


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, unique=True)
    imageSRC = models.CharField(max_length = 1000, null=True, blank=True)
    password = models.CharField(max_length = 100)
