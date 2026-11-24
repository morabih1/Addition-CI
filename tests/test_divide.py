"""Unit tests for Calculator.divide (Chapter 8: component / unit testing)."""
import unittest

from calculator import Calculator


class TestDivide(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_divide_two_positive_numbers(self):
        # Test case from the lecture: divide(10, 2) -> 5.0
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_by_zero_raises_value_error(self):
        # Test case from the lecture: divide(4, 0) -> ValueError("Cannot divide by zero")
        with self.assertRaises(ValueError) as context:
            self.calc.divide(4, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_divide_gives_decimal_result(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_negative_number(self):
        self.assertEqual(self.calc.divide(-9, 3), -3.0)

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_divide_invalid_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.divide("10", 2)


if __name__ == "__main__":
    unittest.main()
