from django.test import TestCase
from watch.models import *

class TestModels(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create('mithila', 'Fossil', 'Digital', 'High demandable watch','A', 50000.0)
        self.product1 = Product.objects.create('mithila', 'Emporio Armani', 'analogue', 'Quality branded Watch','B', 30000.0)
        self.product1 = Product.objects.create('mithila', 'Tissot', 'analogue', 'Best Quality Watch','C', 25000.0)
    

    def test_product_is_assigned(self):
     self.assertEquals(self.product1, 'product-1')



    def test_ ProductImage_model(self):
        self.assertEqual(ProductImage.objects.all().count(), 1)

    