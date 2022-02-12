from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Product(models.Model):

    
     
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=200)
    product_model = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to="products")
    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("watch:detail", kwargs={"pk": self.pk})
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    product_image = models.ImageField(upload_to="products/images/")   

    def __str__(self):
        return self.product.product_name    

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.FloatField()