from django.contrib import admin
from .models import Product, ProductImage, Order


# Register your models here.
admin.site.register([Product,ProductImage])
admin.site.register(Order)