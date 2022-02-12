# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from django.test import SimpleTestCase
from watch.forms import ProductForm

class TestForms(SimpleTestCase):

    def test_product_form_valid_data(self):
        form = ProductForm(data={
            'product_name': 'Fossil',
            'product_category': 'Digital',
            'product_desc': 'High demandable Watch',
            'product_model': 'A',
            'product_price': 50000.0
        })

        self.assertTrue(form.is_valid())

    def test_product_form_no_data(self):
        form = ProductForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)