from django.contrib import admin

from .models import Store, Category, Item

admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Item)
