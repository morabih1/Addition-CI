"""A simple Python program that adds two numbers."""


def add(a, b):
    """Return the sum of two integers or floats."""
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")

    return a + b


def main():
    print("Python Addition Program")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))
    except (ValueError, TypeError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
