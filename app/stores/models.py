from django.conf import settings
from django.db import models


def name_file(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class Store(models.Model):
    registrant = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to=name_file, blank=True, null=True)


class Category(models.Model):
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to=name_file, blank=True, null=True)


class Item(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to=name_file, blank=True, null=True)
