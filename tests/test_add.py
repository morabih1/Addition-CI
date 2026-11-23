"""Unit tests for Calculator.add (Chapter 8: component / unit testing)."""
import unittest

from calculator import Calculator


class TestAdd(unittest.TestCase):
    def setUp(self):
        # Setup part: create the object under test before every test.
        self.calc = Calculator()

    def test_add_two_positive_numbers(self):
        # Test case from the lecture: add(2, 3) -> 5
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-4, -6), -10)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(10, -3), 7)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(7, 0), 7)

    def test_add_decimals(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)

    def test_add_invalid_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.add("5", 3)


if __name__ == "__main__":
    unittest.main()
