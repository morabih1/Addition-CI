"""Unit tests for Calculator.subtract (Chapter 8: component / unit testing)."""
import unittest

from calculator import Calculator


class TestSubtract(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtract_gives_negative_result(self):
        # Test case from the lecture: subtract(5, 8) -> -3
        self.assertEqual(self.calc.subtract(5, 8), -3)

    def test_subtract_positive_result(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-2, -5), 3)

    def test_subtract_same_numbers_gives_zero(self):
        self.assertEqual(self.calc.subtract(9, 9), 0)

    def test_subtract_decimals(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.25), 3.25)

    def test_subtract_invalid_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.subtract(None, 1)


if __name__ == "__main__":
    unittest.main()
