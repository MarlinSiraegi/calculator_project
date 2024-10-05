import unittest
import sys
import os
import math 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator.engineering import EngineeringCalculator

class TestEngineeringCalculator(unittest.TestCase):

    def setUp(self):
        self.eng_calc = EngineeringCalculator()

    def test_add(self):
        self.assertEqual(self.eng_calc.add(1, 2, 3, precision=2), '6.00')

    def test_subtract(self):
        self.assertEqual(self.eng_calc.subtract(10, 2, 3, return_float=True), 5.0)

    def test_multiply(self):
        self.assertEqual(self.eng_calc.multiply(2, 3, 4), 24)

    def test_divide(self):
        self.assertEqual(self.eng_calc.divide(100, 2, precision=3), '50.000')
        with self.assertRaises(Exception):
            self.eng_calc.divide(10, 0)

    def test_square_root(self):
        self.assertEqual(self.eng_calc.square_root(16, precision=3), '4.000')

    def test_power(self):
        self.assertEqual(self.eng_calc.power(2, 3, precision=4), '8.0000')

    def test_log(self):
        self.assertEqual(self.eng_calc.log(100, precision=4), '2.0000')
        self.assertEqual(self.eng_calc.log(8, base=2, precision=3), '3.000')

    def test_ln(self):
        self.assertEqual(self.eng_calc.ln(2.718281828, precision=3), '1.000')

    def test_sin(self):
        self.assertAlmostEqual(float(self.eng_calc.sin(30, angle_units='degree', precision=4)), 0.5000, places=4)
        self.assertAlmostEqual(float(self.eng_calc.sin(math.pi/6, precision=4)), 0.5000, places=4)

    def test_cos(self):
        self.assertAlmostEqual(float(self.eng_calc.cos(60, angle_units='degree', precision=4)), 0.5000, places=4)
        self.assertAlmostEqual(float(self.eng_calc.cos(math.pi/3, precision=4)), 0.5000, places=4)

    def test_tan(self):
        self.assertAlmostEqual(float(self.eng_calc.tan(45, angle_units='degree', precision=4)), 1.0000, places=4)
        self.assertAlmostEqual(float(self.eng_calc.tan(math.pi/4, precision=4)), 1.0000, places=4)

if __name__ == '__main__':
    unittest.main()
