# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
 
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from watch.views import *

class TestUrls(SimpleTestCase):

    def test_index(self):
        url = reverse ('index') 
        self.assertEquals(resolve(url).func, IndexClassView)

    def test_detail(self):
        
        self.assertEqual(resolve(reverse('detail', args=['12345'])).func.view_class, WatchDetail)

    def test_product(self):
        
        self.assertEqual(resolve(reverse('product')).func, product)

    def test_create_product(self):
        
        self.assertEqual(resolve(reverse('create_product')).func, create_product)

    def test_update_product(self):
      
        self.assertEqual(resolve(reverse('update_product', args=['12345'])).func, update_product) 

    def test_remove_product(self):
       
        self.assertEqual(resolve(reverse('remove_product', args=['12345'])).func, remove_product)         

    