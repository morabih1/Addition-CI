"""Simple Calculator - CSCI313 Software Engineering project, Phase 1.

The Calculator class performs the four basic arithmetic operations.
Run this file to use the calculator from the command line:

    python calculator.py
"""
import re

class Calculator:
    """Performs basic arithmetic on two numbers."""

    def _validate(self, a, b):
        """Raise TypeError if a or b is not an int or a float."""
        if type(a) not in (int, float) or type(b) not in (int, float):
            raise TypeError("Both operands must be numbers")

    def add(self, a, b):
        """Return a + b."""
        self._validate(a, b)
        return a + b

    def subtract(self, a, b):
        """Return a - b."""
        self._validate(a, b)
        return a - b

    def multiply(self, a, b):
        """Return a * b."""
        self._validate(a, b)
        return a * b

    def divide(self, a, b):
        """Return a / b. Raise ValueError if b is zero."""
        self._validate(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def format_number(value):
    """Show whole numbers without a trailing .0 (8.0 -> 8)."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)



def evaluate_expression(expression, calc=None):
    """Evaluate one expression such as '2 + 3'."""
    pattern = r"\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*([+\-*/])\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*"
    match = re.fullmatch(pattern, expression)

    if not match:
        raise ValueError("Invalid expression. Example: 2 + 3")

    left, operator, right = match.groups()
    a, b = float(left), float(right)
    calc = calc or Calculator()

    operations = {
        "+": calc.add,
        "-": calc.subtract,
        "*": calc.multiply,
        "/": calc.divide,
    }
    return operations[operator](a, b)

def main(input_func=input, output=print):
    """Run the calculator until the user chooses to quit."""
    calc = Calculator()
    output("=== Simple Calculator ===")

    while True:
        expression = input_func("Enter expression (or q to quit): ").strip()

        if expression.lower() == "q":
            output("Goodbye!")
            return

        try:
            result = evaluate_expression(expression, calc)
        except ValueError as error:
            output(f"Error: {error}")
            continue

        output(f"Result: {expression} = {format_number(result)}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
