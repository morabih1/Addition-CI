"""Unit tests for calculator expression input."""
import unittest

from calculator import evaluate_expression


class TestEvaluateExpression(unittest.TestCase):
    def test_supports_all_four_operations(self):
        examples = {
            "2 + 3": 5,
            "8 - 3": 5,
            "4 * 3": 12,
            "10 / 4": 2.5,
        }

        for expression, expected in examples.items():
            with self.subTest(expression=expression):
                self.assertEqual(evaluate_expression(expression), expected)

    def test_accepts_spaces_and_negative_numbers(self):
        self.assertEqual(evaluate_expression("  -2 + 5  "), 3)

    def test_rejects_invalid_expressions_with_clear_error(self):
        for expression in ("2 +", "hello", "2 ** 3", "nan + 1", "inf / 2"):
            with self.subTest(expression=expression):
                with self.assertRaisesRegex(ValueError, "Invalid expression"):
                    evaluate_expression(expression)

    def test_reports_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            evaluate_expression("5 / 0")
    def test_rejects_numbers_too_large(self):
        with self.assertRaisesRegex(ValueError, "Number is too large"):
            evaluate_expression("9" * 400 + " * 1")



if __name__ == "__main__":
    unittest.main()
