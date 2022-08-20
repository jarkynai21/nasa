from django.db import models
from django.utils import timezone



class Product(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    picture = models.ImageField()
    creation_date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()



class User(models.Model):
    user = models.CharField(max_length=50)
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30, blank=True)


class Discount(models.Model):
    discount = models.IntegerField()
    product = models.ForeignKey(Product, blank=True, null=True, related_name='discount', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    product = models.ForeignKey(Product, blank=True, null=True, related_name='category', on_delete=models.CASCADE)


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, blank=True, null=True, related_name='supplier', on_delete=models.CASCADE)


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.FloatField()
    content = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='Creation date')



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    payment_type = models.CharField(max_length=20)