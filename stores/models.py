from django.conf import settings
from django.db import models


class Store(models.Model):
    registrant = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)


class Category(models.Model):
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)


class Item(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
