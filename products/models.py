from django.db import models

from users.models import User


class ProductsCategories(models.Model):
    name = models.CharField(max_length=126)

    def __str__(self):
        return f"{self.name}"


class Products(models.Model):
    name = models.CharField(max_length=126)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(to=ProductsCategories, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f"{self.name}"


class ImagesProducts(models.Model):
    image = models.ImageField(upload_to='products_images')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.product.name}'


class ProductOptions(models.Model):
    name_detail = models.CharField(max_length=126)
    value = models.CharField(max_length=256)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return f'{self.product.name}'


class Testimonials(models.Model):
    username = models.CharField(max_length=126, default=None)
    text = models.TextField(default=None)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='testimonial')

    def __str__(self):
        return f"{self.username}"


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product:{self.user}.{self.product}"
