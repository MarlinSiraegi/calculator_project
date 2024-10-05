import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator.basic import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2, 3, precision=2), '6.00')

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 2, 3, return_float=True), 5.0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3, 4), 24)

    def test_divide(self):
        self.assertEqual(self.calc.divide(100, 2, precision=3), '50.000')

if __name__ == '__main__':
    unittest.main()
