from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    here we'll define test that run againts products models
    """
    def test_str(self):
        test_name = Product(name= 'A product')
        self.assertEqual(str(test_name), 'A product')