"""Unit tests for Calculator.multiply (Chapter 8: component / unit testing)."""
import unittest

from calculator import Calculator


class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiply_by_zero(self):
        # Test case from the lecture: multiply(4, 0) -> 0
        self.assertEqual(self.calc.multiply(4, 0), 0)

    def test_multiply_two_positive_numbers(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiply_two_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_decimals(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_multiply_invalid_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.multiply([2], 3)


if __name__ == "__main__":
    unittest.main()
