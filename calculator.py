"""Simple Calculator - CSCI313 Software Engineering project, Phase 1.

The Calculator class performs the four basic arithmetic operations.
Run this file to use the calculator from the command line:

    python calculator.py
"""


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


# Menu option -> (operation name, symbol, Calculator method name)
MENU = {
    "1": ("Add", "+", "add"),
    "2": ("Subtract", "-", "subtract"),
    "3": ("Multiply", "*", "multiply"),
    "4": ("Divide", "/", "divide"),
}


def format_number(value):
    """Show whole numbers without a trailing .0 (8.0 -> 8)."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def read_number(prompt, input_func=input, output=print):
    """Keep asking until the user types a valid number."""
    while True:
        text = input_func(prompt).strip()
        try:
            return float(text)
        except ValueError:
            output(f"Error: '{text}' is not a number. Please try again.")


def show_menu(output=print):
    """Print the list of operations."""
    output("")
    output("Choose an operation:")
    for key, (name, symbol, _) in MENU.items():
        output(f"  {key}. {name} ({symbol})")
    output("  q. Quit")


def main(input_func=input, output=print):
    """Run the calculator menu until the user chooses to quit.

    input_func and output can be replaced in tests so the menu
    can be tested without typing on the keyboard.
    """
    calc = Calculator()
    output("=== Simple Calculator ===")

    while True:
        show_menu(output)
        choice = input_func("Your choice: ").strip().lower()

        if choice == "q":
            output("Goodbye!")
            return

        if choice not in MENU:
            output(f"Error: '{choice}' is not a valid choice. Pick 1-4 or q.")
            continue

        name, symbol, method_name = MENU[choice]
        a = read_number("Enter first number: ", input_func, output)
        b = read_number("Enter second number: ", input_func, output)

        try:
            result = getattr(calc, method_name)(a, b)
        except ValueError as error:
            output(f"Error: {error}")
            continue

        output(f"Result: {format_number(a)} {symbol} {format_number(b)} = "
               f"{format_number(result)}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
