import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator.utils import round_result, convert_to_radians

class TestUtils(unittest.TestCase):

    def test_round_result(self):
        self.assertEqual(round_result(3.14159, precision=2), '3.14')
    
    def test_convert_to_radians(self):
        self.assertAlmostEqual(convert_to_radians(180, 'degree'), 3.141592653589793, places=10)

if __name__ == '__main__':
    unittest.main()
