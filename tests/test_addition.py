import unittest
from addition import add


class TestAddition(unittest.TestCase):
    def test_positive(self):
        # Positive test: correct input gives the expected result.
        self.assertEqual(add(5, 3), 8)

    def test_negative(self):
        # Negative test: invalid input raises an error.
        with self.assertRaises(TypeError):
            add("5", 3)


if __name__ == "__main__":
    unittest.main()
