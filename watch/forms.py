from django import forms
from .models import Product,ProductImage

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['product_name','product_category','product_desc','product_model',' product_price','product_image']
        