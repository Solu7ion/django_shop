from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name



class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name