import unittest
from main import *

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a Calculator instance for each test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calculator.add(1, 2), 3)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calculator.subtract(2, 1), 1)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calculator.divide(4, 2), 2)
        self.assertEqual(self.calculator.divide(-4, 2), -2)
        self.assertEqual(self.calculator.divide(-4, -2), 2)

        # Test division by zero
        with self.assertRaises(ValueError):
            self.calculator.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
