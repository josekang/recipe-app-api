from django.test import TestCase

from app.calc import add, subtract

class CalcTest(TestCase):
    
    def test_add_numbers(self):
        """ Add two numbers """
        self.assertEqual(add(5,5), 10)
        
    def test_subtract_numbers(self):
        """ Minus """
        self.assertEqual(subtract(10, 5), 5)