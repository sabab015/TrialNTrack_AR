# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
 
from django.test import TestCase,Client
from django.urls import reverse
import json
from watch.models import *

class testviews(TestCase):

    def setUp (self):
        self.client= Client()
        self.index_url = reverse ('index')
        self.detail_url = reverse ('detail')
        self.product_url = reverse ('product')
        self.create_product_url = reverse ('create')
        self.update_product_url = reverse ('update')
        self.remove_producturl = reverse ('remove')
        self.checkout_url = reverse ('remove')
        self.home_url = reverse ('remove')

    def  test_index_POST(self):
        client = Client()
        response = client.post(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'watch/index.html')

     def test_detail_POST(self):
        client = Client()
        response = client.post(reverse('detail'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'watch/detail.html')
        
    def test_product_POST(self):
            client = Client()
        response = client.post(reverse('product'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'watch/product.html')

    def test_create_product_POST(self):
            client = Client()
        response = client.post(reverse('create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'watch/create.html')

  def test_update_product_POST(self):
            client = Client()
        response = client.post(reverse('update'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'watch/update.html')

   def test_remove_product_POST(self):
            client = Client()
        response = client.post(reverse('remove'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'watch/remove.html')

     def test_checkout_POST(self):
        client = Client()
        response = client.post(reverse('checkout'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'watch/checkout.html') 

     def test_home_POST(self):
        client = Client()
        response = client.post(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'watch/home.html')
     
