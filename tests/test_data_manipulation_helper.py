from decimal import DivisionByZero
import unittest

from DataManipulationModule import data_manipulation_helper


class TestDataManipulationHelper(unittest.TestCase):
    def test_multiply_positives(self):
        self.assertEqual(data_manipulation_helper.multiply(2,3),6)

    def test_multiply_positive_by_negative(self):
        self.assertEqual(data_manipulation_helper.multiply(-2,3),-6)

    def test_multiply_negatives(self):
        self.assertEqual(data_manipulation_helper.multiply(-2,-3),6)

    def test_divide_positives(self):
        self.assertEqual(data_manipulation_helper.divide(3,6),2)

    def test_divide_positive_by_negative(self):
        self.assertEqual(data_manipulation_helper.divide(-3,6),-2)

    def test_divide_negatives(self):
        self.assertEqual(data_manipulation_helper.divide(-3,-6),2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as div:
            data_manipulation_helper.divide(0,1)

if __name__ == '__main__':
    unittest.main()