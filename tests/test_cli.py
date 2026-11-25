"""Tests for the command-line menu (Chapter 8: system / use-case testing).

Each test plays a full scenario a user might go through, using fake
keyboard input, and checks what the calculator prints.
"""
import unittest

from calculator import format_number, main


def run_scenario(inputs):
    """Run the calculator with the given inputs and return everything it printed."""
    answers = iter(inputs)
    printed = []
    main(input_func=lambda prompt: next(answers), output=printed.append)
    return "\n".join(printed)


class TestCalculatorMenu(unittest.TestCase):
    def test_add_then_quit(self):
        output = run_scenario(["5 + 3", "q"])
        self.assertIn("Result: 8", output)
        self.assertIn("Goodbye!", output)

    def test_several_operations_in_one_session(self):
        output = run_scenario(["10 - 4", "6 * 7", "q"])
        self.assertIn("Result: 6", output)
        self.assertIn("Result: 42", output)

    def test_divide_by_zero_shows_error_and_keeps_running(self):
        output = run_scenario(["5 / 0", "9 / 3", "q"])
        self.assertIn("Error: Cannot divide by zero", output)
        self.assertIn("Result: 3", output)

    def test_invalid_expression_shows_error_and_keeps_running(self):
        output = run_scenario(["2 +", "2 + 3", "q"])
        self.assertIn("Error: Invalid expression. Example: 2 + 3", output)
        self.assertIn("Result: 5", output)

    def test_text_expression_shows_error_and_keeps_running(self):
        output = run_scenario(["hello", "2 + 3", "q"])
        self.assertIn("Error: Invalid expression. Example: 2 + 3", output)
        self.assertIn("Result: 5", output)

    def test_format_number(self):
        self.assertEqual(format_number(8.0), "8")
        self.assertEqual(format_number(3.5), "3.5")


if __name__ == "__main__":
    unittest.main()
