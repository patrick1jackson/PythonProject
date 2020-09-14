from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_urls = models.CharField(max_length=2084)


class Offer(models.Model):
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
